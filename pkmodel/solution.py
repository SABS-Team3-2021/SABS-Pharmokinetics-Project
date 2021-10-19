#
# Solution class
#

import typing
from abc import ABC, abstractmethod

class AbstractSolution(ABC):
    # Method to be called on start
    @abstractmethod
    def begin(self, *args, **kwargs): pass

    # Method to be called on completion
    @abstractmethod
    def end(self): pass

    # Reporting method to be called on each iteration
    @abstractmethod
    def report(self, data): pass

    @abstractmethod
    def __getitem__(self, i) -> typing.Tuple: pass

    @abstractmethod
    def writeToFile(self, filename: str): pass

