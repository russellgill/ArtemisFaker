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
import ArtemisFaker
from ArtemisFaker import ModelInterfaceLayer as ifc
from numpy.random import dirichlet, uniform
import numpy as np
import requests
import random
from collections import OrderedDict

class GeneratorClass():

    def __init__(self, size=1):
        name_file = "https://raw.githubusercontent.com/dominictarr/random-name/master/first-names.txt"
        self.names = requests.get(name_file).text
        #self.target_dict = self.generate_od()
        self.names = self.generate_namelist()
    """
    def generate_od(self):
        names = self.generate_namelist()
        od = OrderedDict()
        self.probabilities = dirichlet(np.ones(self.sample),size=1)
        for i, entry in enumerate(self.probabilities[0]):
            od[entry] = names[i]

        return OrderedDict(sorted(od.items()))
    """
    def generate_namelist(self):
        names = self.names.replace("\r", "").split("\n")
        self.sample = len(names)
        return names

    def generate_name(self):
        #key_proto = random.uniform(min(self.probabilities), max(self.probabilities))
        return random.choice(self.names)

class Faker():

    def __init__(self, ProtoMessage):
        self.live_methods = {}
        self.method_names = []
    
    def add_method(self):
        pass

def ExampleNameGen():
    """
    A test replacment for the Faker name generator.
    """

    engine = GeneratorClass()
    params = None
    seed = None
    # Abstract this a little further, insert it into a 
    # wrapper that allows me to feed in a protocol buffer.
    # This will allow us to instantiate an array of methods,
    # and call them by name.
    model_instance = ifc.ModelInterface(
            engine=engine, seed=seed)
    model_instance.custom_generator(method="generate_name", function=False)
    result = model_instance.generate_random()
    print(result)

if __name__ == "__main__":
    ExampleNameGen()