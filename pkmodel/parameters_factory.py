from .parameters.parameters_iv import IV_Parameters
from .parameters.parameters_sub import Subcut_Parameters

class ParametersFactory():
    def getIVParameters():
        return IV_Parameters

    def getSubcutParameters():
        return Subcut_Parameters