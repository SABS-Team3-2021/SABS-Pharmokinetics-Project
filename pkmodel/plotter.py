#
# Abstract Plotting class
#

from abc import ABC, abstractmethod


class AbstractPlotter(ABC):
    """A Pharmokinetic (PK) model

    Parameters
    ----------

    value: numeric, optional
        an example paramter

    """

    @abstractmethod
    def plot(self, filename: str) -> None:
        """
        Plot data in file
        """
        pass

