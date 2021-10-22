from .dataCollectors.dataCollector_numpy import NumpyDataCollector

class DataCollectorFactory():
    def getNumpyDataCollector():
        return NumpyDataCollector