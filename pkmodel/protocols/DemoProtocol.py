# Demo Protocol which is used for solving: dy/dx = -kx.

from ..protocol import AbstractProtocol

class DemoProtocol(AbstractProtocol):
    def __init__(self, *args, **kwargs):
        expected = ['k', 'x0', 'y0']
        for k in expected:
            assert k in kwargs, 'Missing parameter "{}" in input'.format(k)
        self.params = {key: kwargs[key] for key in expected}

    def __getitem__(self, key: str):
        assert key in self.params, 'Invalid Parameter Name'
        return self.params[key]
    
    def properties(self):
        return self.params.keys()
    
    def __str__(self) -> str:
        return str(self.params)
