#
# Abstract Solution class
#

from abc import ABC, abstractmethod
import numpy as np

class AbstractDataCollector(ABC):
    """A Pharmokinetic (PK) model solution

    Takes solutions from the pharmakinetic model at each timestep and stores as a numpy array
    ----------

    value: numeric, optional
        an example paramter

    """

    @abstractmethod
    def begin(self, names: list, number_timesteps: int): pass
    
    @abstractmethod
    def report(self, data) -> None:
        """ Report data as a column vector
        at each timestep
        """
        pass

    @abstractmethod
    def __getitem__(self, i: int) -> np.ndarray:
        """ Return data as a column vector
        """
        pass

    @abstractmethod
    def writeToFile(self, filename: str) -> None:
        """ Write data to a file to be stored
        """
        pass


