from data_collector import AbstractDataCollector
import numpy as np

class Data2NumpyArray(AbstractDataCollector):
    '''
    Class receives data from model and saves to a numpy array
    with an option to write to a csv file
    '''

    def begin(self, names : list , number_timesteps):
        '''
        Initialises a numpy array of a given size, ready to receive data'''
        self.column_length = number_timesteps
        self.column_headers = names
        self.row_width = len(names)
        self.__content= np.zeros(number_timesteps, self.row_width)
        self.__index = 0

    def report(self, data) -> np.array:
        """ Input data as a column vector into the array
        at each timestep
        """
        assert data.shape == (self.row_width, 1)
        self.__content[self.__index, :] = np.transpose(data)
        self.__index += 1

    
    def __getitem__(self, time_point: int) -> np.ndarray:
        """ Return data as a column vector
        at a time point requested. Asserts timepoint is 
        within the 'past' of the model
        """
        assert time_point < self.__index and time_point >= 0 and time_point <= self.column_length
        return np.transpose(self.__content[time_point, :])

    def writeToFile(self, filename: str):
        '''
        Opens a given filename and writes
         data in csv format
         '''
        with open(filename, 'w') as f:
            f.write(','.join(self.__content))
            f.write('\n')
            for i in range(self.column_length):
                f.write(','.join([str(x) for x in self.__content[i,:]]))
                f.write('\n')
