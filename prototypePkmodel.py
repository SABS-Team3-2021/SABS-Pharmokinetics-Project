import pkmodel as pk
from pkmodel.plotters.plotFromCSV import PlotFromCSV
import pandas as pd
import matplotlib.pyplot as plt

numCompartments = 2

params = pk.SubCutNCompParameters(numCompartments,
    CL=1, V_c=1, V_p1=1, V_p2=1, Q_p1=1, Q_p2=1, q_c0=1, q_p1_0=0, q_p2_0=0.5, k_a=1, q_e0=1)
collector = pk.NumpyDataCollector()

model = pk.NComptSubModelScipy(params, collector, 
    pk.create_singlePulse_dosing(0, 0.1, 2), 100, 1000, numCompartments)
model.solve()

collector.writeToFile('test.csv')
