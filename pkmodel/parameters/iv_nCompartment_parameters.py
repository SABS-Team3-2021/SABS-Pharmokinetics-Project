"""Module containing the pharmokinetics (PK) intravenous (IV) parameters class.

It contains a class with a getParam and params_set methods.
"""

from typing import no_type_check
from ..abstractParameters import AbstractParameters


class IVNCompartmentParameters(AbstractParameters):
    """Class in which the parameters for the PK IV model are stored as a
    dictionary.

    It inherits from AbstractParameters.
    """

    def __init__(self, nCompartments, *args, **kwargs):
        expect_params = ['V_c', 'CL', 'q_c0'] + \
            ['Q_p{}'.format(i) for i in range(1, nCompartments+1)] +\
            ['V_p{}'.format(i) for i in range(1, nCompartments+1)] +\
            ['q_p{}_0'.format(i) for i in range(1, nCompartments+1)]
        for param in expect_params:
            assert param in kwargs, 'Missing parameter "{}"'.format(param)
        self.params = {key: kwargs[key] for key in kwargs}

    def getParam(self, key: str) -> float:
        """Returns the parameter associated to a certain key in the dictionary.

        :param key: name associated to the parameter
        :return: parameter associated to the key
        :rtyoe: float
        """
        assert key in self.params
        return self.params[key]

    def getParameterNames(self) -> set:
        """Returns the complete list of parameters, in the form of a dictionary.
        :return: list of parameters and their keys
        :rtype: dictionary
        """
        return self.params.keys()

    def __str__(self) -> str:
        """Convert to string detailing parameters stored in the dictionary.
        : return : Description of parameters
        : rtype : str
        """
        return str(self.params)
