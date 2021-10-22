"""Module containing the pharmokinetics (PK) intravenous (IV) parameters class.

It contains a class with a getParam and params_set methods.
"""

from ..abstractParameters import AbstractParameters


class IV_Parameters(AbstractParameters):
    """Class in which the parameters for the PK IV model are stored as a
    dictionary.

    It inherits from AbstractParameters.
    """

    def __init__(self, *args, **kwargs):
        expect_params = ["Q_p", "V_c", "V_p", "CL", "q_c0", "q_p0"]
        for param in expect_params:
            assert param in kwargs, 'Missing parameter "{}"'.format(param)
        self.params = {key: kwargs[key] for key in kwargs}
        # assert len(self.params) == 4, 'Too many parameters for the IV model'

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
