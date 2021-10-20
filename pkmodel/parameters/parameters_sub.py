from ..abstractParameters import AbstractParameters

class Subcut_Parameters(AbstractParameters):
    '''
    Class stores parameters specifically for the IV system
    as a dictionary
    '''

    def __init__(self, *args, **kwargs):
        expect_params = ['Q_pc', 'V_c', 'V_p', 'CL','k_a', 'q_c0', 'q_p0', 'q_e0']
        for param in expect_params:
            assert param in kwargs, 'Missing parameter "{}"'.format(param)
        self.params = {key : kwargs[key] for key in kwargs}
    
    def getParam(self, key: str) -> float:
        assert key in self.params
        return self.params[key]

    def params_list(self) -> list:
        '''
        Returns a complete list of the the parameters 
        '''
        return self.params.keys()

    def __str__(self) -> str:
        '''
        Return a string representation of the dictionary of paramters
        '''
        return str(self.params)
