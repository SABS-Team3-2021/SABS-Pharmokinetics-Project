#
# Abstract Model class for all models
#

from abc import ABC, abstractmethod

class AbstractModel(ABC):
    @abstractmethod
    def solve(self): pass
