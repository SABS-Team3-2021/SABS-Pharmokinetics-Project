"""Module containing the pharmokinetics abstract data collector class.
"""


from abc import ABC, abstractmethod
import numpy as np


class AbstractDataCollector(ABC):
    """Class in which the Data Collector is abstractly defined.

    The class will receive data from the model (at each timestep) and will save
    the data to a numpy array, with an option to write to a csv file.
    """

    @abstractmethod
    def begin(self, names: list, number_timesteps: int):
        """Initialises a numpy array of a given size, ready to receive data.

        :param names: list of the names of the parameters,
                      used as column headers
        :param number_timesteps: number of time steps in the model resolution,
                                 used to define the columns length
        """
        pass

    @abstractmethod
    def report(self, data: np.ndarray) -> np.array:
        """Report data as a column vector into an array at each timestep.

        :param data: numpy array containing the data of the model resolution
        :return: numpy array containing the model solution
        """
        pass

    @abstractmethod
    def __getitem__(self, i: int) -> np.ndarray:
        """Return data as a column vector at a time point requested. Asserts
        timepoint is within the 'past' of the model.
        """
        pass

    @abstractmethod
    def writeToFile(self, filename: str) -> None:
        """Opens a given filename and writes data in csv format.

        :param filename: name of the file in which the data will be stored
        """
        pass


