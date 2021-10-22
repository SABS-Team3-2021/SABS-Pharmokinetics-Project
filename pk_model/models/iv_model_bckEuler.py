# Model solving the IV dosing set of equations, using backward euler
import typing
import dataclasses
import numpy as np

from ..abstractModel import AbstractModel
from ..abstractParameters import AbstractParameters
from ..abstractDataCollector import AbstractDataCollector


@dataclasses.dataclass
class IVModelBckEuler(AbstractModel):
    parameters: AbstractParameters
    dataCollector: AbstractDataCollector
    doseFn: typing.Callable[[float], float]
    tStop: float
    numIters: int

    def __post_init__(self):
        self.dt = self.tStop / self.numIters

    def eqMatrix(self, t):
        """Generate the Evolution Matrix M and Bias vector b, where M*q_next = q_prev + b
        :param t: float, time
        :returns : np.ndarray matrix M, np.ndarray column vector b
        """
        Q_p = self.parameters.getParam("Q_p")
        V_c = self.parameters.getParam("V_c")
        V_p = self.parameters.getParam("V_p")
        CL = self.parameters.getParam("CL")

        M = np.zeros((2, 2))
        M[0, 0] = 1 + self.dt * CL / V_c + self.dt * Q_p / V_c
        M[0, 1] = self.dt * Q_p / V_p
        M[1, 0] = -self.dt * Q_p / V_c
        M[1, 1] = 1 + self.dt * Q_p / V_p

        b = np.zeros((2, 1))
        b[0, 0] = self.doseFn(t + self.dt) * self.dt
        return M, b

    def solve(self):
        self.dataCollector.begin(
            names=["t", "dose", "q_c", "q_p"], number_timesteps=self.numIters
        )
        self.dataCollector.report(
            np.array(
                [
                    0,
                    self.doseFn(0),
                    self.parameters.getParam("q_c0"),
                    self.parameters.getParam("q_p0"),
                ],
                ndmin=2,
            ).transpose()
        )

        for i in range(1, self.numIters):
            prev = self.dataCollector[i - 1]
            t = prev[0, 0] + self.dt
            dose = self.doseFn(t)

            M, b = self.eqMatrix(t)
            next = np.matmul(np.linalg.inv(M), prev[2:, [0]] + b)

            self.dataCollector.report(np.vstack((t, dose, next)))
