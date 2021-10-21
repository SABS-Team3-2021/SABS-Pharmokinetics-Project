from ..abstractParameters import AbstractParameters

class IV_Parameters(AbstractParameters):
    '''
    Class stores parameters specifically for the IV system
    as a dictionary
    '''

    def __init__(self, *args, **kwargs):
        expect_params = ['Q_pc', 'V_c', 'V_p', 'CL', 'q_c0', 'q_p0']
        for param in expect_params:
            assert param in kwargs, 'Missing parameter "{}"'.format(param)
        self.params = {key : kwargs[key] for key in kwargs}
        # assert len(self.params) == 4, 'Too many parameters for the IV model'
            
    def getParam(self, key: str) -> float:
        assert key in self.params
        return self.params[key]

    def params_set(self) -> set:
        '''
        Returns a complete list of the the parameters 
        '''
        return self.params.keys()

    def __str__(self) -> str:
        '''
        Return a string representation of the dictionary of paramters
        '''
        return str(self.params)
