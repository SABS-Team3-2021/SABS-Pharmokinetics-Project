from .parameters.parameters_iv import IV_Parameters
from .parameters.parameters_sub import Subcut_Parameters
from .parameters.iv_nCompartment_parameters import IVNCompartmentParameters
from .parameters.sub_nCompartment_parameters import SubCutNCompParameters


class ParametersFactory():
    def getIVParameters():
        return IV_Parameters

    def getSubcutParameters():
        return Subcut_Parameters

    def getNCompIVParameters():
        return IVNCompartmentParameters
    
    def getNCompSubCutParameters():
        return SubCutNCompParameters