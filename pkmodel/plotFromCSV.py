from .abstractPlotter import AbstractPlotter
from matplotlib import pyplot as plt
import numpy as np
import csv


class PlotFromCSV(AbstractPlotter):
    '''
    Class which takes CSV-formatted data from a
    given file and returns a matplot,
    with the option to save figure
    '''

    def __init__(self, filename: str, var_names: list):
        '''
        Class is initialised by a .csv containing
        the datapoints, and also requires the list
        of variable names that have been solved for
        in the methods section. This variable name
        list should lead with the time variable
        '''
        self.var_names = var_names
        self.var_number = len(var_names)
        self.data_file = filename

    def plot(self, file_format):
        with open(self.data_file, 'r') as csvfile:
            lines = csv.reader(csvfile, delimiter=',')
        data = np.zeros(len(lines), self.var_number - 1)  # data matrix
        # contains the q values
        time = np.zeros(len(lines))  # time is stored separately for clarity
        i = 0
        for row in lines:
            time[i] = row[0]
            data[i, :] = list(map(int, row[1:]))
            i += 1

        fig, fig_axes = plt.subplots()
        for i in range(self.var_number - 1):
            fig_axes.plot(time, data[i], label=self.var_names[i + 1])
            # recall the first entry of var_names is time so need shifted index

        fig_axes.legend()
        plt.ylabel('drug mass [ng]')
        plt.xlabel('time [h]')
        file_root = self.data_file.split('.')[0]
        fig_file = str(file_root) + '.' + str(file_format)
        fig.savefig(fig_file)  # may need to change which directory it saves in
        plt.show()
