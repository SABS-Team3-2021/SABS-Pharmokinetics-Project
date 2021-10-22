import unittest
from unittest.mock import Mock, MagicMock, call
import numpy as np
import pk_model as pk
from parameterized.parameterized import param, parameterized
import random

numReps = 10
ivSubjects = [pk.IvModelScipy, pk.IVModelBckEuler]
subSubjects = [pk.SubModelScipy, pk.SubModelBckEuler]

class ModelBasicTest(unittest.TestCase):
    
    @parameterized.expand([(s, random.randint(1, 10), random.randint(100, 1000)) for j in range(numReps) for s in ivSubjects+subSubjects])
    def test_construct(self, subject: pk.AbstractModel, endTime: float, numIters: int):
        subject(self.mockParameters, self.mockDataCollector(1), lambda x: 1, endTime, numIters)

    @parameterized.expand([(s, random.randint(1, 10), random.randint(100, 1000)) for j in range(numReps) for s in ivSubjects])
    def test_solveModelIV(self, subject: pk.AbstractModel, endTime: float, numIters: int):
        params = self.mockParameters()
        collector = self.mockDataCollector(4)
        testSubject = subject(params, collector, lambda x: 1, endTime, numIters)
        testSubject.solve()
        for c in [call('Q_p'), call('V_c'), call('V_p'), call('CL'), call('q_c0'), call('q_p0')]:
            self.assertIn(c, params.getParam.call_args_list)
        self.assertEqual(collector.report.call_count, numIters, 'Wrong number of points reported')

    @parameterized.expand([(s, random.randint(1, 10), random.randint(100, 1000)) for j in range(numReps) for s in subSubjects])
    def test_solveModelSci(self, subject: pk.AbstractModel, endTime: float, numIters: int):
        params = self.mockParameters()
        collector = self.mockDataCollector(5)
        testSubject = subject(params, collector, lambda x: 1, endTime, numIters)
        testSubject.solve()
        for c in [call('Q_p'), call('V_c'), call('V_p'), call('CL'), call('k_a'), call('q_e0'), call('q_c0'), call('q_p0')]:
            self.assertIn(c, params.getParam.call_args_list)
        self.assertEqual(collector.report.call_count, numIters, 'Wrong number of points reported')
    
    @parameterized.expand([(n, t, i) for n, t, i in zip(
        [random.randint(1, 5) for j in range(numReps)],
        [random.random()*10 for j in range(numReps)],
        [random.randint(10, 100) for j in range(numReps)]
    )])
    def test_solveModelNIV(self, nCompartments: int, endTime: float, numIters: int):
        params = self.mockParameters()
        collector = self.mockDataCollector(3+nCompartments)
        testSubject = pk.NComptIvModelScipy(params, collector, lambda x: 1, endTime, numIters, nCompartments)
        testSubject.solve()
        for c in [call('V_c'), call('CL'), call('q_c0')] + \
                [call('V_p{}'.format(i)) for i in range(1, nCompartments + 1)] + \
                [call('Q_p{}'.format(i)) for i in range(1, nCompartments+1)] + \
                [call('q_p{}_0'.format(i)) for i in range(1, nCompartments + 1)]:
            self.assertIn(c, params.getParam.call_args_list)
        self.assertEqual(collector.report.call_count, numIters, 'Wrong number of points reported')

    @parameterized.expand([(n, t, i) for n, t, i in zip(
        [random.randint(1, 5) for j in range(numReps)],
        [random.random()*10 for j in range(numReps)],
        [random.randint(10, 100) for j in range(numReps)]
    )])
    def test_solveModelNSubCut(self, nCompartments: int, endTime: float, numIters: int):
        params = self.mockParameters()
        collector = self.mockDataCollector(4+nCompartments)
        testSubject = pk.NComptSubModelScipy(params, collector, lambda x: 1, endTime, numIters, nCompartments)
        testSubject.solve()
        for c in [call('V_c'), call('CL'), call('k_a'), call('q_e0'), call('q_c0')] + \
                [call('V_p{}'.format(i)) for i in range(1, nCompartments + 1)] + \
                [call('Q_p{}'.format(i)) for i in range(1, nCompartments+1)] + \
                [call('q_p{}_0'.format(i)) for i in range(1, nCompartments + 1)]:
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
        