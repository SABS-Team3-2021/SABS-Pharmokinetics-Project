import unittest
from unittest.mock import Mock, MagicMock, call, patch, ANY
import pkmodel as pk
import random
import string
from parameterized.parameterized import parameterized
import numpy as np

numReps = 25

class ApiTest(unittest.TestCase):
    @parameterized.expand([() for i in range(numReps)])
    def test_solve_iv_toFile(self):
        outfilename = ''.join(random.choice(string.ascii_letters) for j in range(15))
        Q_pc, V_c, V_p, CL, q_c0, q_p0 = random.random(),random.random(),random.random(),random.random(),random.random(),random.random()
        doseFn=lambda x: 0
        tSpan, numIters= random.random()*1000, random.randint(100, 1000)
        
        with patch('pkmodel.IV_Parameters.__init__', return_value=None) as mockMakeParams,\
                patch('pkmodel.NumpyDataCollector.__init__', return_value=None) as mockMakeCollector,\
                patch('pkmodel.IvModelScipy.__init__', return_value=None) as mockMakeModel,\
                patch('pkmodel.IvModelScipy.solve') as mockSolve,\
                patch('pkmodel.NumpyDataCollector.writeToFile') as mockWriteFile:
            pk.solve_iv_toFile(outfilename=outfilename, Q_pc=Q_pc, V_c=V_c, V_p=V_p, CL=CL, q_c0=q_c0, q_p0=q_p0,
                doseFn=doseFn, tSpan=tSpan, numIters=numIters)
        mockMakeParams.assert_called_once_with(Q_pc=Q_pc, V_c=V_c, V_p=V_p, CL=CL, q_c0=q_c0, q_p0=q_p0)
        mockMakeCollector.assert_called_once_with()
        mockMakeModel.assert_called_once_with(ANY, ANY, doseFn, tSpan, numIters)
        mockSolve.assert_called_once_with()
        mockWriteFile.assert_called_once_with(outfilename)

    @parameterized.expand([() for i in range(numReps)])
    def test_solve_subcut_toFile(self):
        outfilename = ''.join(random.choice(string.ascii_letters) for j in range(15))
        Q_pc, V_c, V_p, CL, k_a, q_e0, q_c0, q_p0 = random.random(), random.random(), random.random(),random.random(),random.random(),random.random(),random.random(),random.random()
        doseFn=lambda x: 0
        tSpan, numIters= random.random()*1000, random.randint(100, 1000)
        
        with patch('pkmodel.Subcut_Parameters.__init__', return_value=None) as mockMakeParams,\
                patch('pkmodel.NumpyDataCollector.__init__', return_value=None) as mockMakeCollector,\
                patch('pkmodel.SubModelScipy.__init__', return_value=None) as mockMakeModel,\
                patch('pkmodel.SubModelScipy.solve') as mockSolve,\
                patch('pkmodel.NumpyDataCollector.writeToFile') as mockWriteFile:
            pk.solve_subcut_toFile(outfilename=outfilename, Q_pc=Q_pc, V_c=V_c, V_p=V_p, CL=CL, k_a=k_a, q_e0=q_e0, q_c0=q_c0, q_p0=q_p0,
                doseFn=doseFn, tSpan=tSpan, numIters=numIters)
        mockMakeParams.assert_called_once_with(Q_pc=Q_pc, V_c=V_c, V_p=V_p, CL=CL, k_a=k_a, q_e0=q_e0, q_c0=q_c0, q_p0=q_p0)
        mockMakeCollector.assert_called_once_with()
        mockMakeModel.assert_called_once_with(ANY, ANY, doseFn, tSpan, numIters)
        mockSolve.assert_called_once_with()
        mockWriteFile.assert_called_once_with(outfilename)

    @parameterized.expand([() for i in range(numReps)])   
    def test_create_expDecay_dosing(self):
        A, k = random.random()*10, random.random()
        testFn = pk.create_expDecay_dosing(A, k)
        t = random.random()*100
        self.assertEqual(testFn(t), A*np.exp(-np.abs(k)*t))
    
    @parameterized.expand([() for i in range(numReps)])
    def test_create_periodic_dosing(self):
        tHigh, tLow = random.random()*2, random.random()*2
        highVal, lowVal = random.random(), random.random()
        testFn = pk.create_periodic_dosing(tHigh, tLow, highVal, lowVal)
        t = random.random()*100
        self.assertEqual(testFn(t), highVal if t%(tHigh+tLow) <= tHigh else lowVal)