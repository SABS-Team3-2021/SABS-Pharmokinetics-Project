from .parameters.parameters_iv import IV_Parameters
from .dataCollectors.dataCollector_numpy import NumpyDataCollector
from .models.iv_model_scipy import IvModelScipy
from .parameters.parameters_sub import Subcut_Parameters
from .models.sub_model_scipy import SubModelScipy


def solve_iv_toFile(outfilename,
        Q_pc=1, V_c=1, V_p=1, CL=1, q_c0=0, q_p0=0,
        doseFn=lambda x: 0,
        tSpan=1, numIters=1000):
    '''Solve IV Model with given parameters and write solution at each iteration to outfile
    #ADD EXAMPLE USAGE
    # 
    # 
    : param: 
    V_c float: [mL] - the volume of the central compartment
    V_p float: [mL] - the volume of the peripheral compartment
    Q_pc float: the transition rate between central compartment and peripheral compartment 
    CL float: [mL/h] - the clearance/elimination rate from the central compartment
    q_c0 float: [ng] - the initial drug quantity in the central compartment
    q_p0: [ng] - the initial drug quantity in the central compartment
    '''
    params = IV_Parameters(Q_pc=Q_pc, V_c=V_c, V_p=V_p, CL=CL, q_c0=q_c0, q_p0=q_p0)
    soln = NumpyDataCollector()
    model = IvModelScipy(params, soln, doseFn, tSpan, numIters)
    model.solve()
    soln.writeToFile(outfilename)

def solve_subcut_toFile(outfilename,
        Q_pc=1, V_c=1, V_p=1, CL=1, k_a=1, q_e0=0, q_c0=0, q_p0=0,
        doseFn=lambda x: 0,
        tSpan=1, numIters=1000):
    '''Solve IV Model with given parameters and write solution at each iteration to outfile
    #ADD EXAMPLE USAGE
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
    '''
    params = Subcut_Parameters(Q_pc=Q_pc, V_c=V_c, V_p=V_p, CL=CL, q_c0=q_c0, q_p0=q_p0, k_a=k_a, q_e0=q_e0)
    soln = NumpyDataCollector()
    model = SubModelScipy(params, soln, doseFn, tSpan, numIters)
    model.solve()
    soln.writeToFile(outfilename)
