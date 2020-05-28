"""
Copyright © Her Majesty the Queen in Right of Canada, 
as represented by the Minister of Statistics Canada, 2020

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

class ModelInterface():

    def __init__(self, parent, method):
        self.parent = parent  # Assumes instantiated class or method (1)
        self.method = method # The method is loaded (2)
        self.psudo_switch = {"scipy.stats": self.scipygen,
                             "numpy.random": self.numpygen}  # Executes known actions (3)
        
    def generate_random(self, params=None): # Generate the results
        self.params = params  # Set params
        try:
            result = self.psudo_switch[self.parent.__name__] # Grab method from (3)
            return result()
        except (AttributeError, KeyError):
            result = self.custom()  # Othewise get custom method as the "default" for (3)

    def scipygen(self): # For scipy methods
        generator = getattr(self.parent, self.method)
        try:
            
            getattr(generator, "rvs")  # Check if an rvs method
            if self.params:
                return generator(*self.params).rvs()
            else:
                return generator().rvs()

        except AttributeError: # Otherwise skip that
            if self.params:
                return getattr(self.parent, self.method)(*self.params)
            else:
                return getattr(self.parent, self.method)()

    def numpygen(self): # For numpy
        if self.params: # Control for params
            return getattr(self.parent, self.method)(*self.params)
        else:
            return getattr(self.parent, self.method)()

    def custom(self): # For custom code
        if self.params: # Control the params
            return getattr(self.parent, self.method)(*self.params)
        else:
            return getattr(self.parent, self.method)()