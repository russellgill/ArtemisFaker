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
        test_instance = mil.ModelInterface(seed=test_seed)
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

    def test_MIL_params(self):
        """
        Verify that the params can get loaded in.
        """
        test_params = [1, 2, 3]
        test_instance = mil.ModelInterface(params=test_params)
        assert(test_instance.params == test_params)

    def test_MIL_gen_rand(self):
        """
        Verify that the modules
        can load and generate
        randoms.
        """
        entry = "numpy"
        # test without params
        test_instance_no_param = mil.ModelInterface(engine=entry, params=False)
        test_instance_param = mil.ModelInterface(
            engine=entry, params=[9, 1])

        test_instance_no_param.numpy_generator("uniform")
        test_instance_param.numpy_generator("uniform")

        results_no_params = test_instance_no_param.generate_random()
        results_params = test_instance_param.generate_random()
        assert isinstance(results_params, float)
        assert isinstance(results_no_params, float)

    def test_MIL_gen_rand(self):
        """
        Verify that the modules
        can load and generate
        randoms.

        THIS TEST FAILS
        """
        entry = "scipy"
        # test without params
        test_instance_no_param = mil.ModelInterface(engine=entry, params=False)
        test_instance_param = mil.ModelInterface(
            engine=entry, params=[9, 1])

        test_instance_no_param.scipy_generator("normal")
        test_instance_param.scipy_generator("normal")

        results_no_params = test_instance_no_param.generate_random_scipy()
        results_params = test_instance_param.generate_random_scipy()

        print(results_no_params)
        print(results_params)
        assert isinstance(results_params, float)
        assert isinstance(results_no_params, float)


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
    

if __name__ == "__main__":
    unittest.main()
