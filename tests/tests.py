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

from ArtemisFaker import Faker
from importlib import import_module
import unittest


class TestMethod():

    def uniform(self, param):
        return param


class FakerUnitTest(unittest.TestCase):

    def test_numpy_generate(self):
        """
        This is the method that runs
        the generator method. We test
        the output results against the
        results generated by pure numpy.
        """
        seed = 1100  # Our seed value
        method = "normal"  # Our method that we are using
        params = [3, 3]  # These are the params
        module = "numpy.random"

        """
        This is the same process being
        run under the hood in the module
        being tested.
        """
        numpy = import_module(module)  # Import numpy
        numpy.seed(seed)  # Seed it
        rng = getattr(numpy, method)  # Get the generator
        result_base = rng(*params)  # Spit out the result

        """
        This is the method that is testing
        the actual ArtemisFaker method. The
        process being done is the same as
        the one above.
        """
        faker = Faker.ArtemisFaker(seed=seed)  # Instantiate the Faker instance
        faker.add_faker(module, method)  # Add in a faker
        result_test = faker.fake(
            method, params=params)  # Generate the number

        """
        Now we test the results to ensure they
        are correct.
        """
        assert(result_base == result_test)  # Check the equality

    def test_scipy_generate(self):
        """
        This is the method that runs
        the generator method. We test
        the output results against the
        results generated by pure scipy.
        """
        seed = 1100  # Our seed value
        method = "uniform"  # Our method that we are using
        params = [3, 3]  # These are the params
        module = "scipy.stats"  # module name
        numpy = "numpy.random"  # Numpy instance

        """
        This is the same process being
        run under the hood in the module
        being tested.
        """
        numpy = import_module(numpy)
        scipy = import_module(module)  # Import numpy
        numpy.seed(seed)  # Seed it
        rng = getattr(scipy, method)  # Get the generator
        result_base = rng(*params).rvs()  # Spit out the result

        """
        This method will generate the the same
        results as the method above.
        """
        faker = Faker.ArtemisFaker(seed=seed)  # Instantiate the Faker instance
        faker.add_faker(module, method)  # Add in a faker
        result_test = faker.fake(
            method, params=params)  # Generate the number

        assert(result_base == result_test)  # Check the equality

    def test_custom_generate(self):
        """
        This test runs a test
        on the ability of the method
        to accept in a custom class.
        """
        seed = None  # Set the seed
        method = "uniform"  # The method name
        params = [True]  # We will just return the param
        """
        This closed class is a 
        test method that has a 
        single method that returns
        a controlled value.
        """

        provider = TestMethod()  # This is the uninitialized method

        """
        Test the ability to load and access
        the data that is returned out.
        """
        faker = Faker.ArtemisFaker(seed=seed)  # Create faker instance
        faker.add_faker(provider, method)  # Create add faker instance

        results = faker.fake(method, params=params)  # Create the actual result

        assert(results)  # Assert that the result is True


if __name__ == "__main__":

    """
    Pure python test
    """
    params = [True]  # The parameters in the provider
    method = "uniform"  # The name of the provider
    provider = TestMethod()  # Create instance of the target method
    # Get method by regular means, return result
    """
    result = provider.uniform(*params) # This is the method for getting the result from the provider
    result_getattr = getattr(provider, method)(
        *params)  # Get method by name, return result
    assert(result == result_getattr)  # Verify that both the results are equal
    assert(result == True)  # Verify that the result is the boolean value True
    """
    """
    Faker test
    """
    faker = Faker.ArtemisFaker(seed=None)  # Create an artemis faker method
    faker.add_faker(provider, method)  # Inject a faker instance into it
    result = faker.fake(method, params=params)  # Call from the faker instance
    print(result)  # Print out the result
