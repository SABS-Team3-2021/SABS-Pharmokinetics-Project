# Model solving the subcutaneous dosing set of equations, using scipy.
import typing
import numpy as np
import scipy.integrate

from ..abstractModel import AbstractModel
from ..abstractParameters import AbstractParameters
from ..abstractDataCollector import AbstractDataCollector


class SubModelScipy(AbstractModel):
    """ A three compartment (subcutaneous) PK model
    """

    def __init__(self, parameters: AbstractParameters,
                 solution: AbstractDataCollector,
                 dosefunction: typing.Callable[[float], float],
                 timespan: float, nsteps: int):
        self.parameters = parameters
        self. solution = solution
        self.dosefunction = dosefunction
        self.timespan = timespan
        self.nsteps = nsteps

    def solve(self):
        """ Solve IV problem and output to solution.

        It gets the parameters using the parameter class method.

        It writes line by line the solution of the ODEs using
        the solution class method. List format: [time, q_e, q_c, q_p].
        """
        Q_pc = self.parameters.getParam("Q_pc")
        V_c = self.parameters.getParam("V_c")
        V_p = self.parameters.getParam("V_p")
        CL = self.parameters.getParam("CL")
        k_a = self.parameters.getParam("k_a")

        initial_conditions = [self.parameters.getParam("q_c0"),
                              self.parameters.getParam("q_p0"),
                              self.parameters.getParam("q_e0")]
        t_eval = np.linspace(0, self.timespan, self.nsteps)

        def pk_iv_model(t, y, Q_pc, V_c, V_p, CL, k_a):
            """ Returns derivatives for PK IV Model

            Parameters:
            Q_pc : transition rate between central and peripheral
                   compartments (mL/h)
            V_c : volume of central compartment (mL)
            V_p : volume of peripheral compartment (mL)
            CL : clearance/elimination rate from the central compartment (mL/h)
            k_a : absorption rate for the s.c. dosing (/h)

            Returns:
            List containing differential equations, in the form:
            [dqe_dt, dqc_dt, dqp_dt]
            """
            q_e, q_c, q_p = y
            transfer = Q_pc * (q_c / V_c - q_p / V_p)
            dqe_dt = self.dosefunction(t) - k_a * q_e
            dqc_dt = k_a * q_e - q_c / V_c * CL - transfer
            dqp_dt = transfer
            return [dqe_dt, dqc_dt, dqp_dt]

        sol = scipy.integrate.solve_ivp(
            fun=lambda t, y: pk_iv_model(t, y, Q_pc, V_c, V_p, CL, k_a),
            t_span=[t_eval[0], t_eval[-1]],
            y0=initial_conditions, t_eval=t_eval
        )

        t = sol.t
        y = sol.y
        N = t.shape[0]
        columnNames = ["t", "q_e", "q_c", "q_p"]
        self.solution.begin(columnNames, N)
        for i in range(N):
            arr = np.zeros((len(columnNames), 1))
            arr[0] = t[i]
            arr[1:, 0] = y[:, i]
            self.solution.report(arr)
