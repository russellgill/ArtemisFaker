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

from ArtemisFaker import StatisticalModelTemplate as smt
from ArtemisFaker.StatisticalModelTemplate import AbstractModel
from ArtemisFaker import ModelInterfaceLayer as mil
from ArtemisFaker import FakerModelInterfaceLayer as fmil
import importlib as ipl
import unittest
import sys


class TestModelInterfaceLayer(unittest.TestCase):

    def test_MIL_seed(self):
        """
        Verify that seeds can be set.
        """
        test_seed = 11111
        engine = "numpy"
        seeded_np = ipl.import_module("numpy.random")
        seeded_np.seed(test_seed)
        test_instance = mil.ModelInterface(engine=engine)
        test_instance.set_numpy(seeded_np)

        test_instance.numpy_generator("get_state")
        seed_actual = test_instance.generate_random()

        assert(seed_actual[1][0] == test_seed)

    def test_MIL_engine(self):
        """
        Verify that engine can be loaded.
        """
        test_module = "numpy"
        test_instance = mil.ModelInterface(engine=test_module)
        module = test_instance.model
        assert(ipl.import_module(test_module) == module)


    def test_MIL_gen_rand(self):
        """
        Verify that the modules
        can load and generate
        randoms.
        """
        engine = "scipy.stats"
        method = "uniform"
        seed = 1111
        params = [3, 3]

        numpy = ipl.import_module("numpy.random")
        numpy.seed(seed)

        test_result = numpy.uniform(params)
        
        test_instance = mil.ModelInterface()

        test_instance.set_numpy(numpy)

        test_instance.numpy_generator(method)
        
        test_instance.generate_random(params)


class TestStatisticalModelInterfaceLayer(unittest.TestCase):

    def test_set_seed(self):
        model = "numpy.random"
        seed = 1111
        method = "get_state"

        absmod = AbstractModel(model, seed=seed)
        absmod.create_instance(method)
        result = absmod.generate_random()
        assert(result[1][0] == seed)


    def test_create_method(self):
        
        seed = 1111
        method = "sample_method"

        class SampleMethod:

            def seed(self, seedval):
                pass

            def sample_method(self):
                pass
        model = SampleMethod()
        
        absmod = AbstractModel(model, seed=seed, imported=False)
        absmod.create_instance("sample_method")

class TestFakerModelInterfaceLayer(unittest.TestCase):


    def test_generator_factory(self):
        generatable_names = ["first_names_female", "last_names"]
        class_name = "Provider"
        method = "people"
        self.fmil_obj = fmil.FakerRelicShimFactory(class_name, method, generatable_names)
        self.output_check = self.fmil_obj.return_available_generatables()
        assert(len(self.output_check) == len(generatable_names))
        
    def check_method_instantiation(self):
        odpf_obj = None

if __name__ == "__main__":
    unittest.main()
