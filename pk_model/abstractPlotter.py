#
# Abstract Plotting class
#

from abc import ABC, abstractmethod


class AbstractPlotter(ABC):
    """An abstract class which
    can be adapted to various
    plotting methods

    """

    @abstractmethod
    def plot(self, filename: str) -> None:
        """
        Plot data in file
        """
        pass


