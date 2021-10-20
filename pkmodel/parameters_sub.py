from parameters import AbstractParameters

class Subcut_Parameters(AbstractParameters):
    '''
    Class stores parameters specifically for the IV system
    as a dictionary
    '''

    def __init__(self, *args, **kwargs):
        expect_params = ['Q_p1', 'V_c', 'V_p1', 'CL','k_a']
        for param in expect_params:
            assert param in kwargs, 'Missing parameter "{}"'.format(param)
        self.params = {key : kwargs[key] for key in kwargs}
        assert len(self.params) == 4, 'Too many parameters for the IV model'
            
    def __getitem__(self, key: str) -> float:
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
