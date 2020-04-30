import importlib as ipl

class ModelInterface():

    def __init__(self, seed=False, model=None, engine=None, params=False, isDefault=False):
        self.isDefault = isDefault
        self.params = params
        self.engine = engine
        self.seed = seed
        if self.engine is not None:
            if engine.lower() != "scipy" or not seed:
                self.model = ipl.import_module(model)
        if params:
            self.params = params
    
    def custom_generator(self, method):
        """
        Method allowing importing external
        custom synthetic data generators.
        This code provides access to methods
        within the custom generators.
        """
        # Set generator
        generator = getattr(self.model, method)

        # Set seed
        if self.seed:
            set_seed = getattr(self.model, "set_seed")
            set_seed(self.seed)

        # Call generator with or without params
        if self.params:
            return generator(self.params)
        elif not self.params:
            return generator()

    def numpy_generator(self, method):
        """
        Method provides access to numpy
        random number generation tools.
        Allows seeding of generator.
        """
        # Import numpy dynamically
        model = ipl.import_module("numpy.random")
        if self.seed:
            # Now set the seed
            seed_setter = getattr(model, "seed")
            seed_setter(self.seed)

        # Get the specific generator
        self.generator = getattr(model, method)

    def generate_random(self):
        """
        Factory method for returning
        the random number generator.
        """
        model = self.generator
        params = self.params
        if params:
            return model(params)
        else:
            return model()

    def scipy_generator(self, method):
        """
        Method for providing access
        to scipy random number generators.
        May also be seeded.
        """
        # Instantiate the model
        model = ipl.import_module(self.model)
        # Instantiate a numpy instance in the same scope
        if self.seed:
            rng = ipl.import_module("numpy.random")
            # Now set the seed
            seed_setter = getattr(rng, "seed")
            seed_setter(self.seed)

        # Now instantiate the generator
        generator = getattr(model, method)

        # Call generator with
        if self.params:
            return generator().rvs(self.params)
        elif not self.params:
            return generator().rvs()