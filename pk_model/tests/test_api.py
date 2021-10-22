import unittest
from unittest.mock import Mock, MagicMock, call, patch, ANY
import pk_model as pk
import random
import string
from parameterized.parameterized import parameterized
import numpy as np
import pandas as pd
import json
from .config import *
import builtins

numReps = 25
doseFns = [lambda t: 0, lambda t: 1, lambda t: t, lambda t: t*t]

class ApiTest(unittest.TestCase):
    @parameterized.expand([() for i in range(numReps)])
    def test_solve_iv_toFile(self):
        outfilename = ''.join(random.choice(string.ascii_letters) for j in range(15))
        Q_p, V_c, V_p, CL, q_c0, q_p0 = random.random(),random.random(),random.random(),random.random(),random.random(),random.random()
        doseFn=lambda x: 0
        tSpan, numIters= random.random()*1000, random.randint(100, 1000)
        
        with patch('pk_model.IV_Parameters.__init__', return_value=None) as mockMakeParams,\
                patch('pk_model.NumpyDataCollector.__init__', return_value=None) as mockMakeCollector,\
                patch('pk_model.IvModelScipy.__init__', return_value=None) as mockMakeModel,\
                patch('pk_model.IvModelScipy.solve') as mockSolve,\
                patch('pk_model.NumpyDataCollector.writeToFile') as mockWriteFile:
            pk.solve_iv_toFile(outfilename=outfilename, Q_p=Q_p, V_c=V_c, V_p=V_p, CL=CL, q_c0=q_c0, q_p0=q_p0,
                doseFn=doseFn, tSpan=tSpan, numIters=numIters)
        mockMakeParams.assert_called_once_with(Q_p=Q_p, V_c=V_c, V_p=V_p, CL=CL, q_c0=q_c0, q_p0=q_p0)
        mockMakeCollector.assert_called_once_with()
        mockMakeModel.assert_called_once_with(ANY, ANY, doseFn, tSpan, numIters)
        mockSolve.assert_called_once_with()
        mockWriteFile.assert_called_once_with(outfilename)

    def test_solve_subcut_toFile(self):
        outfilename = ''.join(random.choice(string.ascii_letters) for j in range(15))
        Q_p, V_c, V_p, CL, k_a, q_e0, q_c0, q_p0 = random.random(), random.random(), random.random(),random.random(),random.random(),random.random(),random.random(),random.random()
        doseFn=lambda x: 0
        tSpan, numIters= random.random()*1000, random.randint(100, 1000)
        
        with patch('pk_model.Subcut_Parameters.__init__', return_value=None) as mockMakeParams,\
                patch('pk_model.NumpyDataCollector.__init__', return_value=None) as mockMakeCollector,\
                patch('pk_model.SubModelScipy.__init__', return_value=None) as mockMakeModel,\
                patch('pk_model.SubModelScipy.solve') as mockSolve,\
                patch('pk_model.NumpyDataCollector.writeToFile') as mockWriteFile:
            pk.solve_subcut_toFile(outfilename=outfilename, Q_p=Q_p, V_c=V_c, V_p=V_p, CL=CL, k_a=k_a, q_e0=q_e0, q_c0=q_c0, q_p0=q_p0,
                doseFn=doseFn, tSpan=tSpan, numIters=numIters)
        mockMakeParams.assert_called_once_with(Q_p=Q_p, V_c=V_c, V_p=V_p, CL=CL, k_a=k_a, q_e0=q_e0, q_c0=q_c0, q_p0=q_p0)
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

    def test_create_singlePulse_dosing(self):
        tStart, tStop = random.random()*2, random.random()+3
        val = random.random()
        testFn = pk.create_singlePulse_dosing(tStart, tStop, val)
        t = random.random()*5
        self.assertEqual(testFn(t), val if t >= tStart and t < tStop else 0)

    @parameterized.expand([(c,d) for c in modelConfigsSuccess for d in doseFns])
    def test_solveModelFromConfig(self, cfg, doseFn):
        with patch('builtins.open', unittest.mock.mock_open()) as mock_open:
            pk.solve_model_from_config(cfg, doseFn)

    @parameterized.expand([(c, d) for c in modelConfigsFail for d in doseFns])
    def test_solveModelFromConfigFail(self, cfg, doseFn):
        with patch('builtins.open', unittest.mock.mock_open()) as mock_open:
            self.assertRaises(AssertionError, pk.solve_model_from_config, cfg, doseFn)

    @parameterized.expand([({"modelConfig": {}},d, []) for d in doseFns])
    def test_processConfig(self, cfg, doseFn, outfiles):
        with patch('builtins.open', unittest.mock.mock_open()) as mock_open, \
            patch('json.load', return_value = cfg) as cfgPatch, \
            patch('pk_model.api.solve_model_from_config', return_value = outfiles), \
            patch('matplotlib.pyplot'):
            pk.process_config("config", doseFn)
    
    @parameterized.expand([(c,d, []) for d in doseFns for c in fullConfigSuccess])
    def test_processConfigWithPlot(self, cfg, doseFn, outfiles):
        with patch('builtins.open', unittest.mock.mock_open()) as mock_open, \
            patch('json.load', return_value = cfg) as cfgPatch, \
            patch('pk_model.PlotFromCSV.plot'),\
            patch('pandas.read_csv', return_value = pd.DataFrame(data={'t':[1,2],'d':[2,3],'a':[3,4]})):
            pk.process_config("config", doseFn)

    @parameterized.expand([({"aaa": {}},d, []) for d in doseFns])
    def test_processConfigFails(self, cfg, doseFn, outfiles):
        with patch('builtins.open', unittest.mock.mock_open()) as mock_open, \
                patch('json.load', return_value = cfg) as cfgPatch, \
                patch('pk_model.api.solve_model_from_config', return_value = outfiles):
            self.assertRaises(AssertionError,pk.process_config,"config", doseFn)

