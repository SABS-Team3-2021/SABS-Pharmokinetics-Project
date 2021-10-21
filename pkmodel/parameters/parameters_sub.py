"""Module containing the pharmokinetics (PK) subcutaneous (sub) parameters
class.

It contains a class with a getParam and params_set methods.
"""

from ..abstractParameters import AbstractParameters


class Subcut_Parameters(AbstractParameters):
    """Class in which the parameters for the PK sub model are stored as a
    dictionary.

    It inherits from AbstractParameters.
    """

    def __init__(self, *args, **kwargs):
<<<<<<< HEAD
        expect_params = ['Q_pc', 'V_c', 'V_p', 'CL', 'k_a', 'q_c0', 'q_p0', 'q_e0']
        for param in expect_params:
            assert param in kwargs, 'Missing parameter "{}"'.format(param)
        self.params = {key: kwargs[key] for key in kwargs}
    
=======
        expect_params = \
            ['Q_pc', 'V_c', 'V_p', 'CL', 'k_a', 'q_c0', 'q_p0', 'q_e0']
        for param in expect_params:
            assert param in kwargs, 'Missing parameter "{}"'.format(param)
        self.params = {key: kwargs[key] for key in kwargs}

>>>>>>> 547b8dada86b9323b8497c270e707009a08bdb11
    def getParam(self, key: str) -> float:
        """Returns the parameter associated to a certain key in the dictionary.

        :param key: name associated to the parameter to retrieve
        :return: parameter associated to the key
        :rtyoe: float
        """
        assert key in self.params
        return self.params[key]

    def params_list(self) -> list:
<<<<<<< HEAD
        '''
        Returns a complete list of the the parameters
        '''
=======
        """Returns the complete list of parameters, in the form of a dictionary.
        :return: list of parameters and their keys
        :rtype: dictionary
        """
>>>>>>> 547b8dada86b9323b8497c270e707009a08bdb11
        return self.params.keys()

    def __str__(self) -> str:
        """Convert to string detailing parameters stored in the dictionary.
        : return : Description of parameters
        : rtype : str
        """
        return str(self.params)
