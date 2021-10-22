"""Module containing the pharmokinetics (PK) subcutaneous (sub) model class.

It contains a class with a solve method, in which the equations
of the model are defined and solved.
"""

import typing
import numpy as np
import scipy.integrate

from ..abstractModel import AbstractModel
from ..abstractParameters import AbstractParameters
from ..abstractDataCollector import AbstractDataCollector


class SubModelScipy(AbstractModel):
    """Class in which the PK sub model is defined and solved.

    It inherits from AbstractModel.
    It contains the function solve and the subfunction pk_sub_model.
    """

    def __init__(
        self,
        parameters: AbstractParameters,
        solution: AbstractDataCollector,
        dosefunction: typing.Callable[[float], float],
        timespan: float,
        nsteps: int,
    ):
        self.parameters = parameters
        self.solution = solution
        self.dosefunction = dosefunction
        self.timespan = timespan
        self.nsteps = nsteps

    def solve(self):
        """Solves the three compartments PK sub model and outputs to solution.
        It gets the parameters using the parameter class method.
        The solver used is scipy.

        It writes line by line the solution of the ODEs using the solution
        class method.
        Solution format: [time, dose, q_e, q_c, q_p].
        """

        # Definition of the parameters
        Q_p = self.parameters.getParam("Q_p")
        V_c = self.parameters.getParam("V_c")
        V_p = self.parameters.getParam("V_p")
        CL = self.parameters.getParam("CL")
        k_a = self.parameters.getParam("k_a")

        initial_conditions = [
            self.parameters.getParam("q_c0"),
            self.parameters.getParam("q_p0"),
            self.parameters.getParam("q_e0"),
        ]
        t_eval = np.linspace(0, self.timespan, self.nsteps)

        # Definition of the model ODEs
        def pk_sub_model(t, y, Q_p, V_c, V_p, CL, k_a):
            """Defines the differential equations for the PK sub model.

            Parameters:
            :param t: time (h)
            :param y: list of the state variables of the ODEs system, in the
                      form [q_e, q_c, q_p]
            :param Q_p: transition rate between central and peripheral
                         compartments (mL/h)
            :param V_c: volume of central compartment (mL)
            :param V_p: volume of peripheral compartment (mL)
            :param CL: clearance/elimination rate from the central
                       compartment (mL/h)
            :param k_a: absorption rate in the subcutaneous model (/h)

            The parameters (except for t and y) are extracted from the
            Parameter class, using getParam method.

            Returns list containing the differential equations, in the form:
            [dqe_dt, dqc_dt, dqp_dt]
            """
            q_e, q_c, q_p = y
            transfer = Q_p * (q_c / V_c - q_p / V_p)
            dqe_dt = self.dosefunction(t) - k_a * q_e
            dqc_dt = k_a * q_e - q_c / V_c * CL - transfer
            dqp_dt = transfer
            return [dqe_dt, dqc_dt, dqp_dt]

        # Solving the model
        sol = scipy.integrate.solve_ivp(
            fun=lambda t, y: pk_sub_model(t, y, Q_p, V_c, V_p, CL, k_a),
            t_span=[t_eval[0], t_eval[-1]],
            y0=initial_conditions,
            t_eval=t_eval,
        )

        # Feeding the solution line by line to solution class
        t = sol.t
        y = sol.y
        N = t.shape[0]
        columnNames = ["t", "dose", "q_e", "q_c", "q_p"]
        self.solution.begin(columnNames, N)
        for i in range(N):
            arr = np.zeros((len(columnNames), 1))
            arr[0] = t[i]
            arr[1] = self.dosefunction(t[i])
            arr[2:, 0] = y[:, i]
            self.solution.report(arr)
