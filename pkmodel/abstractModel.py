#
# Abstract Model class
#

from abc import ABC, abstractmethod


class AbstractModel(ABC):
    """A Pharmokinetic (PK) model

    Parameters
    ----------

    value: numeric, optional
        an example paramter

    """

    @abstractmethod
    def solve(self):
        """
        Solve using parameters and write output to solution
        """
        pass

