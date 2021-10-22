'''
A detailed example covering both the IV and Subcutaneous models, showing
the break-down where each component of the repository is explicitly used.

Data parameters are manually inputted, the models are solved, with the data
saved to a csv file in the 'example' folder. The data is then plotted
and saved as a .png file.
'''

import pkmodel as pk

# Creates a dose function.
# Here the inbuilt periodic function represents an injection at time 0,
# and again at time 4. A second suggestion gives an exponentially decaying
# dose rate

doseFn = pk.create_periodic_dosing(.2, 4, 2, lowVal=0)
#doseFn = pk.create_expDecay_dosing(1, 1)

# Solves each system and write the output to the example file
pk.solve_iv_toFile('example/exampleIV.csv', 1, 1, 1, 1, 0, 0, doseFn, tSpan=8,
                   numIters=10000)
pk.solve_subcut_toFile('example/exampleSub.csv', 1, 1, 1, 1, 1,
                       0, 0, 0, doseFn, tSpan=8, numIters=10000)

# Takes the data from the csv file, plots and saves the image.
pk.plot_single_file('example/exampleIV.csv')
pk.plot_single_file('example/exampleSub.csv')
