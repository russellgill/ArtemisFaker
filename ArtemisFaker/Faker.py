import numpy.random as random # Random number genreator Numpy
from importlib import import_module # Import module
from ArtemisFaker.MethodHelpers import MethodHandler # Get the method helpers
from ArtemisFaker.ModelHelpers import ModelInterface # Get the model helpers

class ArtemisError(Exception):
    pass

class ArtemisFaker(MethodHandler):

    def __init__(self, seed=None):
        self.numpy = random # Setting the classes RNG backed to be numpy
        super().__init__() # Initiate the superclass
        self.are_avilable = {} # Key-value hashmap for the available methods (1)
        self.seed = seed # Set the seed (2)
        if self.seed is not None: # Check the seed
            self._set_seed() # Set the seed if existant

    def _set_seed(self): 
        """
        Method sets the seed
        for the system.
        """
        self.numpy.seed(self.seed) # Set the seed in the numpy instance from (2)

    def add_faker(self, parent, method):
        """
        This adds the faker instance to the
        hashmap, and gets all the params
        that are needed for instantiating.
        """
        parent = super().get_parent(parent, method) # Fetch the method
        try:
            if parent.__name__ != self.numpy.__name__: # Check if the variable is numpy
                interface = ModelInterface(parent, method) # Create a model interface instance
            else: # If it is, don't use the parent
                interface = ModelInterface(self.numpy, method) # Create the model interface
        except AttributeError:
            interface = ModelInterface(parent, method)
        self.are_avilable[method] = interface # Insert the value into the key value pair (1)
    
    def fake(self, method, params=None):
        """
        This method is the RNG access route,
        and we use it to generate the value.
        What this does it provide an shim to access
        the RNGs with invariate syntax.
        """
        try: # Check if the genrator is inside the hashmap (1)
            interface = self.are_avilable[method] # Get it from the hashmap (1)
            return interface.generate_random(params) # Produce the random value
        except KeyError as error: # Catch the error if it is not instantiated
            raise ArtemisError("Faker method not available.") # Raise an error if it is not there.