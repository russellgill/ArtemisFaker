from ArtemisFaker import StatisticalModelTemplate as smt
from ArtemisFaker import ModelInterfaceLayer as mil
from ArtemisFaker import FakerModelInterfaceLayer as fmil
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

if __name__ == "__main__":
    unittest.main()