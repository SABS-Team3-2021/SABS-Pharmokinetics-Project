#
# Demo Solution to dy/dx = -ky
#

from ..solution import AbstractSolution
import numpy as np
import typing

class DemoNumpySolution(AbstractSolution):
    def begin(self, vars: typing.List[str], N: int):
        self.N = N
        self.vars = vars
        self.data = np.zeros((N, len(vars)))
        self.index = 0

    def __getitem__(self, i):
        assert i < self.index, 'Attempted to access future solution'
        assert i >= 0 and i < self.N, 'Attepmted to access iteration out of possible range'
        return np.transpose(self.data[[i], :])
    
    def report(self, data):
        self.data[[self.index], :] = np.transpose(data)
        self.index += 1

    def end(self):
        pass

    def writeToFile(self, filename: str):
        with open(filename, 'w') as f:
            f.write(','.join(self.vars))
            f.write('\n')
            for i in range(self.data.shape[0]):
                f.write(','.join([str(x) for x in self.data[i,:]]))
                f.write('\n')
