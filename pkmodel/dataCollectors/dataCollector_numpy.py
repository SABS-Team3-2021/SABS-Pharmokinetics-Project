"""Module containing the pharmokinetics data collector class.

It contains a class with begin, report and writetofile methods.
"""

import numpy as np
from ..abstractDataCollector import AbstractDataCollector


class NumpyDataCollector(AbstractDataCollector):
    """Class receives data from model (at each timestep) and saves the data to
    a numpy array, with an option to write to a csv file.
    """

    def begin(self, names: list, number_timesteps: int):
        """Initialises a numpy array of a given size, ready to receive data.

        :param names: list of the names of the parameters,
                      used as column headers
        :param number_timesteps: number of time steps in the model resolution,
                                 used to define the columns length
        """
        self.column_length = number_timesteps
        self.column_headers = names
        self.row_width = len(names)
        self.__content = np.zeros((number_timesteps, self.row_width))
        self.__index = 0

    def report(self, data: np.ndarray) -> np.array:
        """Report data as a column vector into an array at each timestep.

        :param data: numpy array containing the data of the model resolution
        :return: numpy array containing the model solution
        """
        assert data.shape == (self.row_width, 1), 'Invalid Data Shape'
        assert self.__index < self.column_length, \
               'Too many datapoints reported'
        self.__content[self.__index, :] = np.transpose(data)
        self.__index += 1

    def __getitem__(self, time_point: int) -> np.ndarray:
        """Return data as a column vector at a time point requested. Asserts
        timepoint is within the 'past' of the model.

        :param time_point: specified time at which we want the data
        :return: data as a column for the specified time step
        :rtype: numpy array column
        """
        assert (
            time_point < self.__index
            and time_point >= 0
            and time_point <= self.column_length
        )
        return np.transpose(self.__content[[time_point], :])

    def writeToFile(self, filename: str):
        """Opens a given filename and writes data in csv format.

        :param filename: name of the file in which the data will be stored
        """
        with open(filename, "w") as f:
            f.write(",".join(self.column_headers) + '\n')
            for i in range(self.column_length):
                f.write(",".join([str(x) for x in self.__content[i, :]])
                        + '\n')
