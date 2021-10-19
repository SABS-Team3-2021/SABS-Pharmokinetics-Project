#
# Protocol class
#

import typing
from abc import ABC, abstractmethod

class AbstractProtocol(ABC):
    # Return a string explanation of the protocol
    @abstractmethod
    def __str__(self) -> str: pass

    # Get protocol property names
    @abstractmethod
    def properties(self) -> typing.Set[str]: pass

    # Get the protocol property
    @abstractmethod
    def __getitem__(self, key: str): pass


