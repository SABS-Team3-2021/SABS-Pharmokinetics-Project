from .parameters.parameters_iv import IV_Parameters
from .dataCollectors.dataCollector_numpy import NumpyDataCollector
from .models.iv_model_scipy import IvModelScipy

def solve_iv_toFile(outfilename,
        Q_pc=1, V_c=1, V_p=1, CL=1, q_c0=0, q_p0=0,
        doseFn=lambda x: 0,
        tSpan=1, numIters=1000):
    '''Solve IV Model with given parameters and write solution at each iteration to outfile
    #ADD EXAMPLE USAGE
    # 
    # 
    : param: Q_pc float: '''
    params = IV_Parameters(Q_pc=Q_pc, V_c=V_c, V_p=V_p, CL=CL, q_c0=q_c0, q_p0=q_p0)
    soln = NumpyDataCollector()
    model = IvModelScipy(params, soln, doseFn, tSpan, numIters)
    model.solve()
    soln.writeToFile(outfilename)
