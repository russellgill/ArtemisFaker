import numpy.random as random
from importlib import import_module

NUMPY = random

class ArtemisError(Exception):
    pass

class ArtemisFaker(MethodHandler):

    def __init__(self, seed=None):
        super().__init__()
        self.are_avilable = {}
        self.seed = seed # Set the seed
        if self.seed is not None: 
            self._set_seed()

    def _set_seed(self):
        NUMPY.seed(self.seed)

    def add_faker(self, parent, method):
        parent = super().get_parent(parent, method)
        if parent.__name__ != NUMPY.__name__:
            interface = ModelInterface(parent, method)
        else:
            interface = ModelInterface(NUMPY, method)
        self.are_avilable[method] = interface
    
    def fake(self, method, params=None):
        try:
            interface = self.are_avilable[method]
            return interface.generate_random(params)
        except KeyError:
            raise ArtemisError("Faker method not available.")


        