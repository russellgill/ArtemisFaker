from Layers import FakerModelInterfaceLayer, FakerModelInterfaceLayer, StatisticalModelTemplate
from numpy import random

RANDOM = random # Set global RANDOM object. We will use this and pass it around.

class ArtemisFaker():

    def __init__(self, seed=None):
        self.providers = []
        self.random = RANDOM
        if seed:
            self.set_seed(seed)

    def set_seed(self, seed=None):
        try:
            assert(isinstance(seed, int)) or isinstance(seed, float))

        except AssertionError:
            raise ValueError("Falied to set seed. Expected type 'float' or 'int', got %s" %type(seed))

    def add_provider(self, engine, params, isPackage=False):
        if isPackage:
            instance = FakerModelInterfaceLayer.ModelInterface(engine=engine)
        else:
            instance = FakerModelInterfaceLayer.ModelInterface(engine=None)
        return provider