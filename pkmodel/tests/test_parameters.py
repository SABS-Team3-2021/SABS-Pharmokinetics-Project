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

    def test_IVParameters(self):
        self.helperTestConstruct(pk.IV_Parameters, {'Q_p1', 'V_c', 'V_p1', 'CL'})
        self.helperTestRetrieve(pk.IV_Parameters, {'Q_p1', 'V_c', 'V_p1', 'CL'})
        self.assertRaises(AssertionError, self.helperTestConstruct, pk.IV_Parameters, {'Q_p1', 'V_c'})

    def test_SubCutParameters(self):
        self.helperTestConstruct(pk.Subcut_Parameters, {'Q_p1', 'V_c', 'V_p1', 'CL', 'k_a'})
        self.helperTestRetrieve(pk.Subcut_Parameters, {'Q_p1', 'V_c', 'V_p1', 'CL', 'k_a'})
        self.assertRaises(AssertionError, self.helperTestConstruct, pk.Subcut_Parameters, {'Q_p1', 'V_c'})
