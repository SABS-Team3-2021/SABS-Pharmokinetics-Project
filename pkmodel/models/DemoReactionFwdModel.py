#
# Demo Model class used for solving dy/dx = -ky
#

from ..model import AbstractModel
from ..protocol import AbstractProtocol
from ..solution import AbstractSolution

import dataclasses
import typing

import numpy as np

@dataclasses.dataclass
class DemoReactionFwdModel(AbstractModel):
    protocol: AbstractProtocol
    solution: AbstractSolution
    numT: int
    dt: float

    def solve(self):
        self.solution.begin(vars=['theta_1', 'theta_2', 'theta_3', 't'], N=self.numT)
        self.solution.report(np.array([self.protocol['theta_1_0'], self.protocol['theta_2_0'], self.protocol['theta_3_0'], self.protocol['t_0']], ndmin=2).transpose())

        for x in range(1, self.numT):
            prev = self.solution[x-1]

            M = np.zeros((4,4))
            M[0,0] = 1-self.protocol['k_12']*self.dt
            M[1,1] = 1-self.protocol['k_23']*self.dt
            M[1,0] = self.protocol['k_12']*self.dt
            M[2,1] = self.protocol['k_23']*self.dt
            M[2,2] = 1
            M[3,3] = 1
            b = np.zeros((4,1))
            b[3] = self.dt

            next = np.matmul( M, prev) + b
            self.solution.report(next)
        self.solution.end()



