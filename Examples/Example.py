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
from numpy.random import dirichlet, choice
import numpy as np
import requests
from collections import OrderedDict

class GeneratorClass():

    def __init__(self, size=1):
        # Build an array of probs that sums to one
        name_file = "https://raw.githubusercontent.com/dominictarr/random-name/master/first-names.txt"
        self.names = requests.get(name_file).text
        self.target_dict = self.generate_od()

    
    def generate_od(self):
        names = self.generate_namelist()
        od = OrderedDict()
        self.probabilities = dirichlet(np.ones(self.sample),size=1))
        for i, entry in enumerate(probabilities):
            od[entry] = names[i]
        return od

    def generate_namelist(self):
        names = []
        self.sample = 0
        for line in self.names:
            names.append(line.strip("/n"))
            self.sample += 1
        return names

    def generate_name(self):
        key = choice(self.probabilities)
        return self.target_dict[key]



def AtomicEnergies():
    """
    Method generates a simulated atomic state.
    Here we use the package to develop a monte-carlo
    simulation.
    """

    engine = GeneratorClass()
    engine = None
    params = None
    seed = None
    model_instance = ifc.ModelInterface(
            engine=engine, params=params, seed=seed)
    model_instance.external_engine(engine, isFunction=False)
    model_instance.custom_generator("generate_name")
    result = model_instance.generate_random()