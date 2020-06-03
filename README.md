# ArtemisFaker

ArtemisFaker is a random number generator wrapper allowing multiple random number generator methods to be accessed from a single instance. Providing access to both Numpy and Scipy engines natively, as well as custom methods, ArtemisFaker allows the end-user to streamline data generation where multiple techniques are used. 

By implementing the Numpy random number generator as the back-end for the system, the end-user is able to configure an initial state for the system, by seeding the entire instance. Any operations which access the Numpy or Scipy engines will be impacted by the seeding. 

## How it works

ArtemisFaker is broken down into three core components:

Faker.py: serves as a high level abstraction layer between the end-user and the two other underlying components in the system. This component provides an engine-agnostic user-interface to allow the calling of any method, with any generator engine using invariant syntax. 

MethodHelpers.py: provides helpers to lazy-load, as well as verify the validity of a request to a module and method. This module contains the MethodHandler class which executes three main functions: first, it handles the loading in and processing of the module itself. Secondly, the method executes control flows to prevent the overriding of the Numpy seeding in the back-end of the ArtemisFaker module. Finally, the method requested to be loaded is checked against the module provided to verify that it is a valid method in the module. 

ModelHelpers.py: is the deepest level of abstraction in the package and contains the ModelInterface class. Given that Numpy, Scipy and custom generators each need specialized processing to generate the generation step, this class allows random number generation, as well as controls the handling of the parameters passed to the generation modules and methods. Note that this is not an interface design pattern, but rather a class which interfaces with external modules, and user-generated code.

## Workflow Examples

Here is provided a sample work-flow with literate programming notes around it to provide greater clarity as to what each step does.

### Variable definition

We define our variables that will be used
```
>>> seed = 1000
>>> method = ‘normal’
>>> params = [1, 1]
>>> module = ‘numpy.random’
```

The core variables have been defined to show the control available to the user.

### Creating the instance of ArtemisFaker

Now we will instantiate an instace of ArtemisFaker by calling the ArtemisFaker module.

```
>>> from ArtemisFaker import Faker
>>> fake = Faker(seed=seed)
```

We call Faker and pass it the arg seed, which is defined as 1000 above. At this point, we now have an instance of our ArtemisFaker module, which runs the Numpy RNG back-end. We have also seeded the system. Any subsequent methods called, will start from that RNG initial state.

#### Techincal Notes

Under-the-hood, there's a little bit going on here. First, the back-end is set to numpy as the first step of execution. Next, the super-class MethodHandler is initiated as a ```super()``` object. We then create a class-variable called ```self.seed```. After, if the seed is not ```None```, ```self._set_seed()``` is called allowing the generator state to be set. Once this process is completed, the base of ArtemisFaker is configured and set.

### Load the module

We now load in our method to the instance of ArtemisFaker.

```
>>> fake.add_faker(module, method)
```

This has now loaded in the module to ArtemisFaker. The module is made accesable by the name of the method that is being called. These are stored as a key-value pair in the module. What this means is that, to access the module for generating random numbers, all that must be done is request, by name, the generator method. The engine is no longer needed in the call, as the generator is not simply handled as an ArtemisFaker generator.

#### Techincal Notes

```fake.add_faker(parent, method)``` is a rather involved process. The super-class calls it's method ```super().get_parent(parent, method)```. This method is also rather involved. Before getting into the details, it is important to note that the entire purpose of this method is to return an object to the ArtemisFaker intance which is callable later on.

Under-the-hood, the method sets the module in ```self.parent```. The control-sequence verifies that the method and the parent are both strings. This senario causes the methods to be lazy-imported. Should this not be the case, and the user has presented a callable method to the ```fake.add_faker(parent, method)``` method, an ```AssertionError``` is triggered. In the catch block, the method is checked to verify that it is not Numpy. If it is, infact Numpy, to avoid overwriting the state of the RNG back-end, Numpy is not imported, and the back-end's instance of Numpy is used to provide the random number generation. Otherwise, the module quickly checked to verify that the requested method is contained in the module. Should this test pass, the module is returned back to the Faker class. 

In the case that this is neither numpy, nor a callable, the class loads the module, and from there checks if the method is contained. Once this is completed, the method then returns the callable to Faker. Once returned back to the Faker instance, a ModelInterface instance is created which contains the parent and the target method. This is then loaded into a hashmap/dictonary to allow retreval later.

### Generating a random number

Now that we have the system staged, we can generate a random number.
```
>>> result = faker.fake(method, params=params)
>>> result
0.67
```

#### Technical Notes

The random number generation requires different control logic depending on what random number generation method is being called. For instance, while with numpy you can simply call ```numpy.random.uniform(*params)```, whereas with scipy, you have to call ```scipy.stats.normal(*params).rvs()``` for some instances. To properly capture this behaviour, the ModelInterface which was created later is accessed by key. We then access the ```interface.generate_random(params)``` method. 

Inside the ```interface.generate_random(params)```, a switch like argument is executed to determine if the method is scipy-based or numpy-based. If either of these are the case, the dedicated methods are called. Otherwise, the default condition of the custom method generator is called. 

As things become very general at this point, we will look at the custom generator. Once this method is called, we check if ```self.params```'s state has been changed from the default of ```None```. If this is the case, the method is fetched by name with ```getattr(generator, method)``` and passed params. Otherwise, the generator is called without params. The result of the execution is returned to the Faker module. The value is then returned to the main program.

### Instances with multiple fakers

The generators, when loaded into the ArtemisFaker module, are called fakers. We can load more than one faker into our ArtemisFaker instance, insofar as there is no name-collision between the generators, now fakers. Future areas for improvment would be allowing loading fakers that would have otherwise resulted in a name-collision. 

```
>>> fakers = [('numpy.random', 'uniform'), ('scipy.stats', 'poisson')]
>>> for entry in fakers:
>>>   fake.add_faker(entry[0], entry[1])
>>> fake.fake('poisson', [0, 0])
```

Here we load in the modules in a loop. We are able to load in all the methods, and access them at will using the 
## Project Upkeep Considerations

ArtemisFaker has been designed with developer friendliness in mind. We are moving towards a per-line documentation approach. Providing clear, but short explanations of each execution step helps reduce time invested in understanding the code base. Descriptive variable names are also used, with variables and methods being identified by snake_case. Classes and modules are identified with CamelCase. Variable name verbosity is increased proportionally to the distance away from the variable assignment, with only temporary variables (ie loop incrementers) being given single character names. 

