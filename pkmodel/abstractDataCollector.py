from abc import ABC, abstractmethod
import numpy as np


class AbstractDataCollector(ABC):
    """Abstract class for the Data Collector.

    Class receives data from model and saves to a numpy array
    with an option to write to a csv file.

    """

    @abstractmethod
    def begin(self, names: list, number_timesteps: int):
        """Initialises a numpy array of a given size, ready to receive data.

        :param names: list of the variables' names
        :param number_timesteps: number of time steps in the model's resolution
        """
        pass

    @abstractmethod
    def report(self, data) -> None:
        """Input data as a column vector into the array at each timestep

        :param data: numpy array of the data to report
        :return: data in the right shape
        :rtype: numpy array
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

        :param filename: name of the file to open
        """
        pass


