import unittest
from unittest.mock import Mock, MagicMock, call
import numpy as np
import pkmodel as pk
from parameterized.parameterized import parameterized
import random

numReps = 10
ivSubjects = [pk.IvModelScipy, pk.IVModelBckEuler]
subSubjects = [pk.SubModelScipy, pk.SubModelBckEuler]

class ModelTest(unittest.TestCase):
    
    @parameterized.expand([(s, random.randint(1, 10), random.randint(100, 1000)) for j in range(numReps) for s in ivSubjects+subSubjects])
    def test_construct(self, subject: pk.AbstractModel, endTime: float, numIters: int):
        subject(self.mockParameters, self.mockDataCollector(1), lambda x: 1, endTime, numIters)

    @parameterized.expand([(s, random.randint(1, 10), random.randint(100, 1000)) for j in range(numReps) for s in ivSubjects])
    def test_solveModelIV(self, subject: pk.AbstractModel, endTime: float, numIters: int):
        params = self.mockParameters()
        collector = self.mockDataCollector(3)
        testSubject = subject(params, collector, lambda x: 1, endTime, numIters)
        testSubject.solve()
        for c in [call('Q_pc'), call('V_c'), call('V_p'), call('CL'), call('q_c0'), call('q_p0')]:
            self.assertIn(c, params.getParam.call_args_list)
        self.assertEqual(collector.report.call_count, numIters, 'Wrong number of points reported')

    @parameterized.expand([(s, random.randint(1, 10), random.randint(100, 1000)) for j in range(numReps) for s in subSubjects])
    def test_solveModelSci(self, subject: pk.AbstractModel, endTime: float, numIters: int):
        params = self.mockParameters()
        collector = self.mockDataCollector(4)
        testSubject = subject(params, collector, lambda x: 1, endTime, numIters)
        testSubject.solve()
        for c in [call('Q_pc'), call('V_c'), call('V_p'), call('CL'), call('k_a'), call('q_e0'), call('q_c0'), call('q_p0')]:
            self.assertIn(c, params.getParam.call_args_list)
        self.assertEqual(collector.report.call_count, numIters, 'Wrong number of points reported')
        
    def mockParameters(self):
        mock = Mock()
        mock.getParam.return_value = 1
        return mock

    def mockDataCollector(self, numCols):
        mock = MagicMock()
        mock.__getitem__.return_value = np.zeros((numCols, 1))
        return mock
        