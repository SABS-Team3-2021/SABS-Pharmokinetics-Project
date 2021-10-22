import unittest
from parameterized import parameterized
import pk_model as pk
import random

numReps = 1000

class DoseFnTests(unittest.TestCase):
    @parameterized.expand([(random.random()*100, random.random()*100+100, random.random()*10, random.random()*200) for j in range(numReps)])
    def test_PulseFn(self, start, stop, dose, check):
        doseFn = pk.blockPulse()
        doseFn.add_pulse(start, stop, dose)
        self.assertEqual(doseFn(check), dose if check >= start and check < stop else 0)
