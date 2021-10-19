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
class DemoModel(AbstractModel):
    protocol: AbstractProtocol
    solution: AbstractSolution
    numX: int
    dx: float

    def solve(self):
        self.solution.begin(vars=['x', 'y'], N=self.numX)
        self.solution.report(np.array([self.protocol['y0'], self.protocol['x0']], ndmin=2).transpose())

        for x in range(1, self.numX):
            prev = self.solution[x-1]
            next = np.matmul( np.array([[1-self.protocol['k']*self.dx, 0], [0, 1]]), prev) + np.array([0, self.dx], ndmin=2).transpose()
            self.solution.report(next)
        self.solution.end()



