from ArtemisFaker import StatisticalModelTemplate as smt
from ArtemisFaker.StatisticalModelTemplate import AbstractModel
from ArtemisFaker import ModelInterfaceLayer as mil
from ArtemisFaker import FakerModelInterfaceLayer as fmil
import importlib as ipl
import unittest
import sys

engine = "scipy.stats"
method = "norm"
seed = 1111
params = [3, 3]

numpy = ipl.import_module("numpy.random")
numpy.seed(seed)

model = ipl.import_module(engine)
generator = getattr(model, method)
results = generator(*params).rvs()

del numpy

test_instance_param = mil.ModelInterface(
    engine=engine, params=params, seed=seed)
test_instance_param.scipy_generator(method)
results_params = test_instance_param.generate_random_scipy(rvs=True)

assert(results_params == results)
assert(type(results) == type(results_params))
