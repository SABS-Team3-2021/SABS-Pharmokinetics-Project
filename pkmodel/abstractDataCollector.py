#
# Abstract Solution class
#

from abc import ABC, abstractmethod
import numpy as np

class AbstractSolution(ABC):
    """A Pharmokinetic (PK) model solution

    Parameters
    ----------

    value: numeric, optional
        an example paramter

    """
    
    @abstractmethod
    def report(self, data) -> None:
        """ Report data as a column vector
        """
        pass

    @abstractmethod
    def __getitem__(self, i: int) -> np.ndarray:
        """ Return data as a column vector
        """
        pass

    @abstractmethod
    def writeToFile(self, filename: str) -> None:
        pass


