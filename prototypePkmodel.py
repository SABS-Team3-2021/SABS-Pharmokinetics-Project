import pkmodel as pk
from pkmodel.plotters.plotFromCSV import PlotFromCSV
import pandas as pd
import matplotlib.pyplot as plt

pk.process_config('config.json', pk.create_singlePulse_dosing(0, 0.1, 1))
