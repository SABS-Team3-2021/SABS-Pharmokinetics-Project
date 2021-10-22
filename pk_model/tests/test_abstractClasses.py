import unittest
import pk_model as pk

class TestAbstractClasses(unittest.TestCase):
    def test_AbstractDataCollector(self):
        pk.AbstractDataCollector.begin(None, 0, 0)
        pk.AbstractDataCollector.report(None, 0)
        pk.AbstractDataCollector.__getitem__(None, 0)
        pk.AbstractDataCollector.writeToFile(None, '')

    def test_AbstractParameters(self):
        pk.AbstractParameters.getParam(None, '')
        pk.AbstractParameters.getParameterNames(None)
        pk.AbstractParameters.__str__(None)
    
    def test_AbstractModel(self):
        pk.AbstractModel.solve(None)

    def test_AbstractPlotter(self):
        pk.AbstractPlotter.plot(None, '')
