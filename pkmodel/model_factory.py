from .models.iv_model_scipy import IvModelScipy
from .models.sub_model_scipy import SubModelScipy


class ModelFactory():
    def getIvModelScipy():
        return IvModelScipy
    
    def getSubModelScipy():
        return SubModelScipy
    
