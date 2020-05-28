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
        self.parent = parent  # Assumes instantiated class or method
        self.method = method # The method
        self.psudo_switch = {"scipy.stats": self.scipygen,
                             "numpy.random": self.numpygen}  # Executes known actions
        
    def generate_random(self, params=None): # Generate the results
        self.params = params  # Set params
        try:
            result = self.psudo_switch[self.parent.__name__]  # Grab method
            return result()
        except KeyError:
            print("Failure")
            result = self.custom()  # Othewise get custom method

    def scipygen(self): # For scipy methods
        try:
            getattr(self.method, "rvs")  # Check if an rvs method
            if self.params:
                return getattr(self.parent, self.method)(*self.params).rvs()
            else:
                return getattr(self.parent, self.method)().rvs()

        except AttributeError: # Otherwise skip that
            if params:
                return getattr(self.parent, self.method)(*self.params)
            else:
                return getattr(self.parent, self.method)()

    def numpygen(self): # For numpy
        if self.params: # Control for params
            return getattr(self.parent, self.method)(*self.params)
        else:
            return getattr(self.module, self.method)()

    def custom(self): # For custom code
        if self.params: # Control the params
            return getattr(self.parent, self.method)(*self.params)
        else:
            return getattr(self.module, self.method)()