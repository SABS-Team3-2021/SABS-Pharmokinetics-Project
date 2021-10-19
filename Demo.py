import pkmodel
import pandas as pd
import matplotlib.pyplot as plt

### Demo 1
'''
demoProtocol = pkmodel.DemoProtocol(k=1, x0=0, y0=10)
print(demoProtocol)

demoSolution = pkmodel.DemoNumpySolution()

demoModel = pkmodel.DemoModel(demoProtocol, demoSolution, 1000, 0.01)

demoModel.solve()

demoSolution.writeToFile('data/demo1.csv')
#'''

### Demo 2
reactionProtocol = pkmodel.DemoReactionProtocol(k_12 = 1, k_23 = 0.5, theta_1_0 = 1, theta_2_0 = 0, theta_3_0 = 0, t_0 = 0)
reactionFwdSolution = pkmodel.DemoNumpySolution()

numT = 1000
dt = 0.01

reactionFwdModel = pkmodel.DemoReactionFwdModel(reactionProtocol, reactionFwdSolution, numT, dt)
reactionFwdModel.solve()
reactionFwdSolution.writeToFile('data/reactionFwdSolution.csv')


#Solve same protocol using different solver
reactionBckSolution = pkmodel.DemoNumpySolution()
reactionBckModel = pkmodel.DemoReactionBckModel(reactionProtocol, reactionBckSolution, numT, dt)
reactionBckModel.solve()
reactionBckSolution.writeToFile('data/reactionBckSolution.csv')

dataFwd = pd.read_csv('data/reactionFwdSolution.csv')
dataBck = pd.read_csv('data/reactionBckSolution.csv')

def plot(data):
    plt.plot(data['t'], data['theta_1'])
    plt.plot(data['t'], data['theta_2'])
    plt.plot(data['t'], data['theta_3'])
    plt.show()