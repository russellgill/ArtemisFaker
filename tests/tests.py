from ArtemisFaker import StatisticalModelTemplate as smt
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
        print(results_no_params)
        print(results_params)
        assert isinstance(results_params, float)
        assert isinstance(results_no_params, float)


if __name__ == "__main__":
    unittest.main()
