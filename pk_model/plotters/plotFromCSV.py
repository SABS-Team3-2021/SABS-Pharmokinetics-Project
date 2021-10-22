# from pandas.io.parsers import read_csv
# from matplotlib.lines import _LineStyle  # not sure if any of these needed
import numpy as np
from ..abstractPlotter import AbstractPlotter
from matplotlib import pyplot as plt
import pandas as pd


class PlotFromCSV(AbstractPlotter):
    '''
    Class which takes CSV-formatted data from a
    given file and returns a matplot,
    with the option to save figure
    '''

    def __init__(self, filename: str):
        '''
        Class is initialised by a .csv containing
        the datapoints, with headers giving the list
        of variable names that have been solved for
        in the methods section. This variable name
        list should lead with the time variable
        '''
        self.data_file = filename

    def plot(self, file_format):
        '''
        Function which takes a csv data file, reads it and separates the data
        into different variables including dose and time. Outputs a plot of
        each variable on the same plot and saves to a given file format
        '''
        full_data = pd.read_csv(self.data_file, delimiter=',')
        # Read_csv outputs a data frame first column is time, second column is
        # the dose at each timepoint.
        var_names = full_data.columns.tolist()
        var_number = len(var_names)
        full_data = pd.DataFrame(full_data).to_numpy()
        time = full_data[:, 0]
        dose = full_data[:, 1]
        data = full_data[:, 2:]
        fig, axes1 = plt.subplots()
        colours = plt.cm.viridis(np.linspace(0, .67, var_number))
        for i in range(var_number - 2):
            axes1.plot(time, data[:, i], color=colours[i], 
                       label=var_names[i + 2])
        axes1.plot([], [], color='r', linestyle='dashed', label='Dose')
        # recall the first two entries of var_names are time and dose,
        # so need shifted index

        axes1.set_ylabel('drug mass [ng]')
        axes1.legend()
        plt.xlabel('time [h]')
        axes2 = axes1.twinx()
        axes2.set_ylabel('dose [ng/h]')
        axes2.plot(time, dose, color='r', linestyle='dashed', label='Dose')
        axes1.legend()
        fig.tight_layout()
        file_root = self.data_file.split('.')[0]
        fig_file = str(file_root) + '.' + str(file_format)
        fig.savefig(fig_file)  # may need to change which directory it saves in
        plt.show()
