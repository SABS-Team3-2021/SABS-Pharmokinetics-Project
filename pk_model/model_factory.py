from .models.iv_model_scipy import IvModelScipy
from .models.sub_model_scipy import SubModelScipy
from .models.iv_model_ncompt_scipy import NComptIvModelScipy
from .models.sub_model_ncompt_scipy import NComptSubModelScipy


class ModelFactory():
    def getIvModelScipy():
        return IvModelScipy
    
    def getSubModelScipy():
        return SubModelScipy
    
    def getNCompIVModel():
        return NComptIvModelScipy
    
    def getNCompSubCutModel():
        return NComptSubModelScipy