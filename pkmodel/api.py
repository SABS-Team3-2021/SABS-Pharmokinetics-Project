from .model_factory import ModelFactory
from .dataCollector_factory import DataCollectorFactory
from .parameters_factory import ParametersFactory
from .plotter_factory import PlotterFactory
import numpy as np

def solve_iv_toFile(outfilename,
        Q_pc=1, V_c=1, V_p=1, CL=1, q_c0=0, q_p0=0,
        doseFn=lambda x: 0,
        tSpan=1, numIters=1000):
    '''Solve IV Model with given parameters and write solution at each iteration to outfile
    # 
    # 
    : param: 
    V_c float: [mL] - the volume of the central compartment
    V_p float: [mL] - the volume of the peripheral compartment
    Q_pc float: the transition rate between central compartment and peripheral compartment 
    CL float: [mL/h] - the clearance/elimination rate from the central compartment
    q_c0 float: [ng] - the initial drug quantity in the central compartment
    q_p0: [ng] - the initial drug quantity in the central compartment

    Usage::

      >>> import pkmodel as pk
      >>> pk.solve_iv_toFile("outData.csv", Q_pc=1, V_c=1, doseFn=lambda t: 1, tSpan=100, numIters=1000)
      >>> import pandas as pd
      >>> pd.read_csv("outData.csv")
                  t  dose       q_c       q_p
0      0.0000   1.0  0.000000  0.000000
1      0.1001   1.0  0.090864  0.004540
2      0.2002   1.0  0.166024  0.016509
3      0.3003   1.0  0.228892  0.033884
4      0.4004   1.0  0.282140  0.055095
..        ...   ...       ...       ...
995   99.5996   1.0  0.999833  1.000103
996   99.6997   1.0  0.999866  1.000083
997   99.7998   1.0  0.999881  1.000073
998   99.8999   1.0  0.999890  1.000068
999  100.0000   1.0  0.999906  1.000058

[1000 rows x 4 columns]

    '''
    params = ParametersFactory.getIVParameters()(Q_pc=Q_pc, V_c=V_c, V_p=V_p, CL=CL, q_c0=q_c0, q_p0=q_p0)
    soln = DataCollectorFactory.getNumpyDataCollector()()
    model = ModelFactory.getIvModelScipy()(params, soln, doseFn, tSpan, numIters)
    model.solve()
    soln.writeToFile(outfilename)

def solve_subcut_toFile(outfilename,
        Q_pc=1, V_c=1, V_p=1, CL=1, k_a=1, q_e0=0, q_c0=0, q_p0=0,
        doseFn=lambda x: 0,
        tSpan=1, numIters=1000):
    '''Solve IV Model with given parameters and write solution at each iteration to outfile
    # 
    # 
    : param: 
    V_c float: [mL] - the volume of the central compartment
    V_p float: [mL] - the volume of the peripheral compartment
    Q_pc float: the transition rate between central compartment and peripheral compartment 
    CL float: [mL/h] - the clearance/elimination rate from the central compartment
    q_c0 float: [ng] - the initial drug quantity in the central compartment
    q_p0 float: [ng] - the initial drug quantity in the central compartment
    k_a float: [/h] - the “absorption” rate from the entrance compartment for the subcutaneous dosing
    q_e0 float: [ng] - the initial drug quantity in the entrance compartment

    Usage::

      >>> import pkmodel as pk
      >>> pk.solve_subcut_toFile("outData.csv", Q_pc=1, V_c=1, doseFn=lambda t: 1, tSpan=100, numIters=1000)
      >>> import pandas as pd
      >>> pd.read_csv("outData.csv")
                        t  dose       q_e       q_c       q_p
0      0.0000   1.0  0.000000  0.000000  0.000000
1      0.1001   1.0  0.095253  0.004540  0.000151
2      0.2002   1.0  0.181433  0.016511  0.001099
3      0.3003   1.0  0.259404  0.033883  0.003372
4      0.4004   1.0  0.329948  0.055102  0.007281
..        ...   ...       ...       ...       ...
995   99.5996   1.0  1.000000  1.000024  0.999985
996   99.6997   1.0  1.000000  1.000276  0.999829
997   99.7998   1.0  1.000000  1.000539  0.999667
998   99.8999   1.0  1.000000  1.000717  0.999557
999  100.0000   1.0  1.000000  1.000687  0.999575

[1000 rows x 5 columns]


    '''
    params = ParametersFactory.getSubcutParameters()(Q_pc=Q_pc, V_c=V_c, V_p=V_p, CL=CL, q_c0=q_c0, q_p0=q_p0, k_a=k_a, q_e0=q_e0)
    soln = DataCollectorFactory.getNumpyDataCollector()()
    model = ModelFactory.getSubModelScipy()(params, soln, doseFn, tSpan, numIters)
    model.solve()
    soln.writeToFile(outfilename)


def create_expDecay_dosing(A: float, k: float):
    """ Create an Exponentially decaying dosing profile (A*exp(-k*t))
    : param: A float: Dose at t=0
    : param: k float: Dosing decay rate
    : returns: Dosing Profile
    : rtype: Callable[[float], float]
    """
    def inner(t: float) -> float:
        return A * np.exp(-np.abs(k)*t)
    return inner

def create_periodic_dosing(timeHigh, timeLow, highVal, lowVal=0):
    """ Create a Periodic dosing profile
    # ------------------------------------------------------------
    # Create a dosing profile which oscillates between high and low values.
    # Remains high for timeHigh and low for lowHigh each period
    # ------------------------------------------------------------
    : param: timeHigh float: Time dosing remains at highVal
    : param: timeLow float: Time dosing remains at lowVal
    : param: highVal float: dosing ammount during high levels
    : param: lowVal float: dosing level during low levels
    : returns: Dosing Profile
    : rtype: Callable[[float], float]
    """
    def inner(t: float) -> float:
        phase = t%(timeHigh+timeLow)
        return highVal if phase <= timeHigh else lowVal
    return inner
