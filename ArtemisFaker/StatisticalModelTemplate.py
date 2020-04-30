import importlib as ipl

class AbstractModel():

    def __init__(self):
        pass

    def set_seed(self, seed):
        """
        Method for setting seeds.
        """
        seed = ipl.import_module("numpy.random")
        self.set_seed = getattr(self.model, "set_seed")
        self.set_seed(self.seed)
    
    def generator(self, method, params=False):
        """
        Method for configuring the seeds
        for a system.
        """
        if self.seed:
            seed = self.set_seed()
        # Inject methods or processes here.
        if params:
            return method(params)
        else:
            return method()