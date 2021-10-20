#
# Abstract Parameter class
#

from abc import ABC, abstractmethod

class AbstractParameters(ABC):
    """A Pharmokinetic (PK) protocol

    Parameters
    ----------

    value: numeric, optional
        an example paramter

    """
    
    @abstractmethod
    def setParam(self, key: str, val: float) -> None: pass

    @abstractmethod
    def getParam(self, key: str) -> float:
        """Retrieve Parameter
        : param key : parameter name to retrieve
        : return : parameter value
        : rtype : float
        """
        pass

    @abstractmethod
    def __str__(self) -> str:
        """Convert to string detailing parameters stored
        : return : Description of parameters
        : rtype : str
        """
        pass

    
