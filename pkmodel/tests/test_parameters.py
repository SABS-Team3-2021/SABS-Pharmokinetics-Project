import unittest
import pkmodel as pk
import random

class TestParameters(unittest.TestCase):
    """
    Tests the 'AbstractParameters' classes
    """
    
    def helperTestConstruct(self, testClass: pk.AbstractParameters, paramNames: set) -> None:
        testParams = {key: random.random() for key in paramNames}
        testSubject = testClass(**testParams)

    def helperTestRetrieve(self, testClass: pk.AbstractParameters, paramNames: set) -> None:
        testParams = {key: random.random() for key in paramNames}
        testSubject = testClass(**testParams)
        for key in testParams:
            self.assertEqual(testParams[key], testSubject.getParam(key))

    def helperTestStr(self, testClass: pk.AbstractParameters, paramNames: set) -> None:
        testParams = {key: random.random() for key in paramNames}
        testSubject = testClass(**testParams)
        self.assertEqual(str(testParams), str(testSubject))

    def helperTestGetKeys(self, testClass: pk.AbstractParameters, paramNames: set) -> None:
        testParams = {key: random.random() for key in paramNames}
        testSubject = testClass(**testParams)
        self.assertEqual(testParams.keys(), testSubject.getParameterNames())

    def test_IVParameters(self):
        self.helperTestConstruct(pk.IV_Parameters, {'Q_pc', 'V_c', 'V_p', 'CL', 'q_c0', 'q_p0'})
        self.helperTestRetrieve(pk.IV_Parameters, {'Q_pc', 'V_c', 'V_p', 'CL', 'q_c0', 'q_p0'})
        self.assertRaises(AssertionError, self.helperTestConstruct, pk.IV_Parameters, {'Q_pc', 'V_c'})
        self.helperTestStr(pk.IV_Parameters, {'Q_pc', 'V_c', 'V_p', 'CL', 'q_c0', 'q_p0'})
        self.helperTestGetKeys(pk.IV_Parameters, {'Q_pc', 'V_c', 'V_p', 'CL', 'q_c0', 'q_p0'})

    def test_SubCutParameters(self):
        self.helperTestConstruct(pk.Subcut_Parameters, {'Q_pc', 'V_c', 'V_p', 'CL', 'k_a', 'q_c0', 'q_p0', 'q_e0'})
        self.helperTestRetrieve(pk.Subcut_Parameters, {'Q_pc', 'V_c', 'V_p', 'CL', 'k_a', 'q_c0', 'q_p0', 'q_e0'})
        self.assertRaises(AssertionError, self.helperTestConstruct, pk.Subcut_Parameters, {'Q_pc', 'V_c'})
        self.helperTestStr(pk.Subcut_Parameters, {'Q_pc', 'V_c', 'V_p', 'CL', 'k_a', 'q_c0', 'q_p0', 'q_e0'})
        self.helperTestGetKeys(pk.Subcut_Parameters, {'Q_pc', 'V_c', 'V_p', 'CL', 'k_a', 'q_c0', 'q_p0', 'q_e0'})
    
