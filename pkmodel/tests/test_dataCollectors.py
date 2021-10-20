import unittest
from unittest.suite import TestSuite
from parameterized import parameterized
import pkmodel as pk
import random
import os
import pandas as pd
import numpy as np
import string

def generateFnHelperNumpyArray(n: int):
    def inner():
        return np.random.random((n, 1))
    return inner

subjects = [pk.Data2NumpyArray]
generateFnHelpers = [generateFnHelperNumpyArray]
compareFns = [lambda a,b: a.all()==b.all()]

class DataCollectorTests(unittest.TestCase):
    @parameterized.expand([(s,) for s in subjects])
    def test_Construct(self, subject):
        testSubject = subject()
        testSubject.begin(self.helperCols(2), 5)
    
    @parameterized.expand([(s,t,c,i) for s, t in zip(subjects, generateFnHelpers)
        for c, i in zip([5, 10]+[random.randint(10, 100) for j in range(20)], [10, 50]+[random.randint(50, 100) for j in range(20)])])
    def test_reportTest(self, subject, generateFnHelper, numCols: int, numIters: int):
        testSubject = subject()
        testSubject.begin(self.helperCols(numCols), numIters)
        self.mockReport(testSubject, generateFnHelper(numCols), numIters)

    @parameterized.expand([(s,t,cmp,c,i) for s, t, cmp in zip(subjects, generateFnHelpers, compareFns)
        for c, i in zip([5, 10]+[random.randint(10, 100) for j in range(20)], [10, 50]+[random.randint(50, 100) for j in range(20)])])
    def test_reportRetrieveTest(self, subject, generateFnHelper, compareFn, numCols: int, numIters: int):
        testSubject = subject()
        testSubject.begin(self.helperCols(numCols), numIters)
        data = self.mockReport(testSubject, generateFnHelper(numCols), numIters)
        self.mockRetrieveAndVerify(testSubject, data, compareFn)

    @parameterized.expand([(s,t) for s, t in zip(subjects, generateFnHelpers)])
    def test_WriteFile(self, subject, generateFnHelper):
        testSubject = subject()
        nCols, nIters = random.randint(2,10), random.randint(10, 100)
        testSubject.begin(self.helperCols(nCols), nIters)
        self.mockReport(testSubject, generateFnHelper(nCols), nIters)
        filename = ''.join(random.choice(string.ascii_letters) for i in range(15))
        testSubject.writeToFile(filename)
        pd.read_csv(filename)
        os.remove(filename)
    
    @parameterized.expand([(s,t) for s, t in zip(subjects, generateFnHelpers)])
    def test_FailRetrieve(self, subject, generateFnHelper):
        testSubject = subject()
        nCols, nIters = 2, 5
        testSubject.begin(self.helperCols(nCols), nIters)
        self.helperTestFailRetrieve(testSubject, generateFnHelper(nCols))
    
    def helperTestFailRetrieve(self, testSubject, generateFn):
        self.assertRaises(AssertionError, testSubject.__getitem__, -1)
        self.assertRaises(AssertionError, testSubject.__getitem__, 0)
        self.mockReport(testSubject, generateFn, 3)
        testSubject.__getitem__(2)
        testSubject.__getitem__(0)
        self.assertRaises(AssertionError, testSubject.__getitem__, 3)
        self.assertRaises(AssertionError, testSubject.__getitem__, -2)
    
    def helperCols(self, numCols: int) -> list:
        return [''.join(random.choice(string.ascii_letters) for i in range(10)) for j in range(numCols)]
    
    def mockReport(self, testSubject, generateFn, numIterations):
        data = []
        for i in range(numIterations):
            data.append(generateFn())
            testSubject.report(data[i])
        return data
    
    def mockRetrieveAndVerify(self, testSubject, data, compareFn):
        for i in range(len(data)):
            retrieved = testSubject[i]
            self.assertTrue(compareFn(data[i], retrieved),
                'Expected {}, but {} was returned.'.format(data[i], retrieved))
