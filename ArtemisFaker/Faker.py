import numpy.random as random # Random number genreator Numpy
from importlib import import_module # Import module
from ArtemisFaker.MethodHelpers import MethodHandler # Get the method helpers
from ArtemisFaker.ModelHelpers import ModelInterface # Get the model helpers

class ArtemisError(Exception):
    pass

class ArtemisFaker(MethodHandler):

    def __init__(self, seed=None):
        self.numpy = random
        super().__init__()
        self.are_avilable = {} # Key-value hashmap for the available methods
        self.seed = seed # Set the seed
        if self.seed is not None: # Check the seed
            self._set_seed() # Set the seed if existant

    def _set_seed(self): 
        """
        Method sets the seed
        for the system.
        """
        self.numpy.seed(self.seed) # Set the seed in the numpy instance

    def add_faker(self, parent, method):
        parent = super().get_parent(parent, method) # Fetch the method
        if parent.__name__ != self.numpy.__name__: # Check if the variable is numpy
            interface = ModelInterface(parent, method) # 
        else:
            interface = ModelInterface(self.numpy, method)
        self.are_avilable[method] = interface
    
    def fake(self, method, params=None):
        try:
            interface = self.are_avilable[method]
            return interface.generate_random(params)
        except KeyError as error:
            raise ArtemisError("Faker method not available.")