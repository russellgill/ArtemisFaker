import importlib as ipl
from numpy.random import choice

"""
Factory class that produces shim
giving access to Faker provider
methods within a provider class.
Returns a dict containing the method
name, as well as the 'live' method.
"""
class FakerRelicShimFactory():

    def __init__(self,ClassName, ProviderName, GeneratableNames):
        self.orderedDicts = []
        self.methods = {}
        self.generatableNames = GeneratableNames
        self.liveClass = getattr(ipl.import_module(ProviderName), ClassName)
        self.get_available_ordered_dicts()
    
    def get_available_ordered_dicts(self):
        """
        Instantiates access to all the entries in
        which include methods an attributes. Will
        allow user to pull in both variables, as well
        as methods and functions.
        """
        for method in self.generatableNames:
            self.methods[method] = getattr(self.liveClass, method)
    
    def return_available_generatables(self):
        """
        Returns back the self.methods object.
        """
        return self.methods
    
    def help(self):
        """
        Returns out a list of the attributes
        to the class called. Useful for loading
        a new provider without having read it.
        """
        return vars(self.liveClass)

"""
Generates an ordered dictonary provider from
a fed in schema using the FakerRelicShimFactory
to provide access to the ordered dicts within
the old generator method.
"""
class ODProviderFactory(FakerRelicShimFactory):

    def __init__(self, ClassName, ProviderName, GeneratableNames, DatumSchema, UseFaker=True, GeneratorDicts=None):
	if UseFaker is True:
		super().__init__(ClassName, ProviderName, GeneratableNames)
		self.generators = super().return_available_generatables()
        self.available_methods = {}
    elif UseFaker is False:
        self.available_methods = GeneratorDicts
    self.schema = DatumSchema

    def produce_available_methods(self, GeneratorList):
        """
        Takes in a list of dicts containing list name
        and the list of item, weight pairs.
        """
        for generator in GeneratorList:
            for name, arrays in generator.items():
                generatable = arrays["generatables"]
                weights = arrays[""]
                self.available_methods[name] = {}

    def createDatum(self, Seperator=" "):
        """
        Create datum from format array and argument array
        Implements numpy RNG system. Functions for all
        ordered dict generation procedures.
        """ 
        output = ""
        i = 0
        end = len(self.schema) 
        for method in self.schema:
            i -=- 1 
            method_dict = self.available_methods[method]
            injection = choice(method_dict["generatables"], 1, p=method_dict["weights"])
            if i != end:
                output = output + injection[0] + Seperator
            else:
                output = output + injection[0]

        return output
