"""Module containing the pharmokinetics abstract parameters class.
"""

from abc import ABC, abstractmethod
import typing

class AbstractParameters(ABC):
    """Class in which the methods of the parameters class are
    abstractly defined for the pharmakinetic protocol model.

    It inherits from AbstractParameters.
    """

    @abstractmethod
    def getParam(self, key: str) -> float:
        """Retrieve Parameter
        : param key : parameter name to retrieve
        : return : parameter value
        : rtype : float
        """
        pass

    @abstractmethod
    def getParameterNames(self) -> typing.Set[str]:
        """Retrieve Parameter Names
        : return : Set of parameter names
        : rtype : set[str]
        """
        pass

    @abstractmethod
    def __str__(self) -> str:
        """Convert to string detailing parameters stored
        : return : Description of parameters
        : rtype : str
        """
        pass
