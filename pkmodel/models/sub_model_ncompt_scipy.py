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


class NComptSubModelScipy(AbstractModel):
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
        ncompartments: int,
    ):
        self.parameters = parameters
        self.solution = solution
        self.dosefunction = dosefunction
        self.timespan = timespan
        self.nsteps = nsteps
        self.ncompartments = ncompartments

    def solve(self):
        """Solves the three compartments PK sub model and outputs to solution.
        It gets the parameters using the parameter class method.
        The solver used is scipy.

        It writes line by line the solution of the ODEs using the solution
        class method.
        Solution format: [time, dose, q_e, q_c, q_p].
        """

        # Definition of the parameters
        V_c = self.parameters.getParam("V_c")
        CL = self.parameters.getParam("CL")
        k_a = self.parameters.getParam("k_a")

        initial_conditions = [0 for i in range(self.ncompartments + 2)]
        initial_conditions[0] = self.parameters.getParam("q_e0")
        initial_conditions[1] = self.parameters.getParam("q_c0")
        for i in range(1, self.ncompartments + 1):
            initial_conditions[i + 1] = self.parameters.getParam("q_p{}_0".format(i))

        t_eval = np.linspace(0, self.timespan, self.nsteps)

        # Definition of the model ODEs
        def pk_sub_model(t, q):
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
            result = [0 for i in range(2 + self.ncompartments)]
            result[0] = self.dosefunction(t) - q[0] * k_a
            result[1] = q[0] * k_a - q[1] * CL / V_c
            for i in range(1, 1 + self.ncompartments):
                Q_p = self.parameters.getParam("Q_p{}".format(i))
                V_p = self.parameters.getParam("V_p{}".format(i))
                result[i + 1] = Q_p * (q[1] / V_c - q[i + 1] / V_p)
                result[1] -= result[i + 1]
            return result

        # Solving the model
        sol = scipy.integrate.solve_ivp(
            fun=pk_sub_model,
            t_span=[t_eval[0], t_eval[-1]],
            y0=initial_conditions,
            t_eval=t_eval,
        )

        # Feeding the solution line by line to solution class
        t = sol.t
        y = sol.y
        N = t.shape[0]
        columnNames = ["t", "dose", "q_e", "q_c"] + [
            "q_p{}".format(i) for i in range(1, self.ncompartments + 1)
        ]
        self.solution.begin(columnNames, N)
        for i in range(N):
            arr = np.zeros((len(columnNames), 1))
            arr[0] = t[i]
            arr[1] = self.dosefunction(t[i])
            arr[2:, 0] = y[:, i]
            self.solution.report(arr)
