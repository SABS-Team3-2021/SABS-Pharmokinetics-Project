"""
A detailed example covering both the IV and Subcutaneous models, showing
the break-down where each component of the repository is explicitly used.

Data parameters are manually inputted, the models are solved, with the data
saved to a csv file in the 'example' folder. The data is then plotted
and saved as a .png file.
"""

import pkmodel as pk

# Manually set model parameters and initial conditions for the IV model
paramsIV = pk.IV_Parameters(
    Q_p=1.0,
    V_c=1.0,
    V_p=1.0,
    CL=1.0,
    q_c0=0.0,
    q_p0=0.0,
)

# Manually set parameters and initial conditions for the
# subcutaneous model
paramsSub = pk.Subcut_Parameters(
    Q_p=1.0, V_c=1.0, V_p=1.0, CL=1.0, k_a=0.5, q_c0=0.0, q_p0=0.0, q_e0=0.0
)

# Creates a dose function.
# Here the inbuilt blockpulse function represents an injection at time 0.
doseFn = pk.blockPulse()
doseFn.add_pulse(0, 0.1, 1.0)

# Initialises a data structure to receive the output from the model solution.
# The data cllector structure will work for eiher model
solnScipyIV = pk.NumpyDataCollector()
solnScipySub = pk.NumpyDataCollector()

# Initialises the pharmakinetic model solver, inputing parameters,
# solution structure, dose function, maximum time and number of timesteps.
modelScipyIV = pk.IvModelScipy(paramsIV, solnScipyIV, doseFn, 10, 10000)
modelScipySub = pk.SubModelScipy(paramsSub, solnScipySub, doseFn, 10, 10000)

# Solves the model uses the solver class.
modelScipyIV.solve()
modelScipySub.solve()

# Saves the data as a .csv file in the example folder
solnScipyIV.writeToFile("example/iv_scipy.csv")
solnScipySub.writeToFile("example/sub_scipy.csv")

# Takes the data from the csv file, plots and saves the image.
pk.PlotFromCSV("example/iv_scipy.csv").plot("png")
pk.PlotFromCSV("example/sub_scipy.csv").plot("png")
