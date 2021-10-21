import pkmodel as pk
from pkmodel.plotters.plotFromCSV import PlotFromCSV
import pandas as pd
import matplotlib.pyplot as plt

'''
params = pk.IV_Parameters(
        Q_pc= 1.0,
        V_c= 1.0,
        V_p= 1.0,
        CL= 1.0,
        q_c0= 0.0,
        q_p0= 0.0,
)
solnScipy = pk.NumpyDataCollector()
solnEuler = pk.NumpyDataCollector()

def doseFn(x: float) -> float: return x*x

modelScipy = pk.IvModelScipy(params, solnScipy, doseFn, 0.01, 1000)
modelEuler = pk.IVModelBckEuler(params, solnEuler, doseFn, 0.01, 1000)
modelScipy.solve()
modelEuler.solve()

solnScipy.writeToFile('iv_scipy.csv')
solnEuler.writeToFile('iv_euler.csv')

scipyData = pd.read_csv('iv_scipy.csv')
eulerData = pd.read_csv('iv_euler.csv')

plt.plot(scipyData['t'], scipyData['q_p'])
plt.plot(eulerData['t'], eulerData['q_p'])
plt.show()
#'''

def doseFn(t: float) -> float: return 1

pk.solve_iv_toFile(outfilename = 'data.csv', Q_pc=1, V_c=1, V_p=1, CL=1, q_c0=0, q_p0=0, doseFn=doseFn, numIters=1000, tSpan=1)
