import unittest
from unittest.mock import Mock, MagicMock, call
import numpy as np
import pkmodel as pk
from parameterized.parameterized import param, parameterized
import random
import typing

reps = 10
ivSubjects = [pk.IvModelScipy, pk.IVModelBckEuler]
subSubjects = [pk.SubModelScipy, pk.SubModelBckEuler]

def generateIVParams(reps: int):
    return [pk.IV_Parameters(Q_p=1,V_c=1,V_p=1,CL=1,q_c0=random.random(),q_p0=random.random())for j in range(reps)]

def generateSubParams(reps: int):
    return [pk.Subcut_Parameters(Q_p=1,V_c=1,V_p=1,CL=1,k_a=1,q_e0=0,q_c0=0,q_p0=0)for j in range(reps)]



def generateDoseFns(reps: int):
    def getDoseFn():
        a = random.random()
        b = random.random()
        def inner(t: float) -> float:
            return a*t + b*t*t
        return inner
    return [getDoseFn() for j in range(reps)]

class ModelCompareTest(unittest.TestCase):

    @parameterized.expand([(s1, s2, p, d, t, n) for s1 in ivSubjects for s2 in ivSubjects if s1!=s2 for p, d, t, n in zip(generateIVParams(reps), generateDoseFns(reps), [random.random()/1000 for j in range(reps)], [random.randint(1000, 2000) for j in range(reps)])])
    def test_ivCompare(self, subject1: pk.AbstractModel, subject2: pk.AbstractModel, params: pk.AbstractParameters, doseFn: typing.Callable[[float], float], tSpan: float, numIters: int):
        sol1, sol2 = pk.NumpyDataCollector(), pk.NumpyDataCollector()
        testSubject1 = subject1(params, sol1, doseFn, tSpan, numIters)
        testSubject2 = subject2(params, sol2, doseFn, tSpan, numIters)
        testSubject1.solve()
        testSubject2.solve()
        self.helperCompare(sol1, sol2, numIters)

    @parameterized.expand([(s1, s2, p, d, t, n) for s1 in subSubjects for s2 in subSubjects if s1!=s2 for p, d, t, n in zip(generateSubParams(reps), generateDoseFns(reps), [random.random()/1000 for j in range(reps)], [random.randint(1000, 2000) for j in range(reps)])])
    def test_subCompare(self, subject1: pk.AbstractModel, subject2: pk.AbstractModel, params: pk.AbstractParameters, doseFn: typing.Callable[[float], float], tSpan: float, numIters: int):
        sol1, sol2 = pk.NumpyDataCollector(), pk.NumpyDataCollector()
        testSubject1 = subject1(params, sol1, doseFn, tSpan, numIters)
        testSubject2 = subject2(params, sol2, doseFn, tSpan, numIters)
        testSubject1.solve()
        testSubject2.solve()
        self.helperCompare(sol1, sol2, numIters)

    def helperCompare(self, sol1, sol2, numIters):
        point1, point2 = sol1[numIters-1], sol2[numIters-1]
        for i in range(point1.shape[0]):
            self.assertAlmostEqual(point1[i,0], point2[i,0], 1, "Models don't agree")


    

