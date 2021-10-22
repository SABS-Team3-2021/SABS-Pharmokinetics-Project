"""Module containing the pharmokinetics (PK) intravenous (IV) model class.

It contains a class with a solve method, in which the equations
of the model are defined and solved.
"""

import typing
import numpy as np
import scipy.integrate

from ..abstractModel import AbstractModel
from ..abstractParameters import AbstractParameters
from ..abstractDataCollector import AbstractDataCollector


class NComptIvModelScipy(AbstractModel):
    """Class in which the PK IV model is defined and solved.

    It inherits from AbstractModel.
    It contains the function solve and the subfunction pk_iv_model.
    """

    def __init__(
        self,
        parameters: AbstractParameters,
        solution: AbstractDataCollector,
        dosefunction: typing.Callable[[float], float],
        timespan: float,
        nsteps: int,
        ncompartments: int,
    ):
        self.parameters = parameters
        self.solution = solution
        self.dosefunction = dosefunction
        self.timespan = timespan
        self.nsteps = nsteps
        self.ncompartments = ncompartments

    def solve(self):
        """Solves the two compartments PK IV model and outputs to solution.

        It gets the parameters using the parameter class method.
        The solver used is scipy.

        It writes line by line the solution of the ODEs using the solution
        class method.
        Solution format: [time, dose, q_c, q_p].
        """

        # Definition of the parameters
        V_c = self.parameters.getParam("V_c")
        CL = self.parameters.getParam("CL")
        initial_conditions = [0 for i in range(self.ncompartments + 1)]
        initial_conditions[0] = self.parameters.getParam("q_c0")
        for i in range(1, self.ncompartments + 1):
            initial_conditions[i] = self.parameters.getParam("q_p{}_0".format(i))
        t_eval = np.linspace(0, self.timespan, self.nsteps)

        # Definition of the model ODEs
        def pk_iv_model(t, q):
            """Defines the differential equations for the PK IV model.

            Parameters:
            :param t: time (h)
            :param y: list of the state variables of the ODEs system, in the
                      form [q_c, q_p]
            :param Q_p: transition rate between central and peripheral
                         compartments (mL/h)
            :param V_c: volume of central compartment (mL)
            :param V_p: volume of peripheral compartment (mL)
            :param CL: clearance/elimination rate from the central
                       compartment (mL/h)

            The parameters (except for t and y) are extracted from the
            Parameter class, using getParam method.

            Returns list containing the differential equations, in the form:
            [dqc_dt, dqp_dt]
            """
            result = [0 for i in range(1 + self.ncompartments)]
            result[0] = self.dosefunction(t) - q[0] * CL / V_c
            for i in range(1, 1 + self.ncompartments):
                Q_p = self.parameters.getParam("Q_p{}".format(i))
                V_p = self.parameters.getParam("V_p{}".format(i))
                result[i] = Q_p * (q[0] / V_c - q[i] / V_p)
                result[0] -= result[i]
            return result

        # Solving the model
        sol = scipy.integrate.solve_ivp(
            fun=pk_iv_model,
            t_span=[t_eval[0], t_eval[-1]],
            y0=initial_conditions,
            t_eval=t_eval,
        )

        # Feeding the solution line by line to solution class
        t = sol.t
        y = sol.y
        N = t.shape[0]
        columnNames = ["t", "dose", "q_c"] + [
            "q_p{}".format(i) for i in range(1, self.ncompartments + 1)
        ]
        self.solution.begin(columnNames, N)
        for i in range(N):
            arr = np.zeros((len(columnNames), 1))
            arr[0] = t[i]
            arr[1] = self.dosefunction(t[i])
            arr[2:, 0] = y[:, i]
            self.solution.report(arr)
