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

from importlib import import_module

class MethodHandler():

    def get_parent(self, parent, method):
        self.parent = parent
        try:
            assert isinstance(method, str) and isinstance(parent, str)
            self.method = method # Set the method
        except AssertionError:
            try: # Check if numpy, will trip only if seeded
                assert not self._is_numpy()
                self._check_child()
                return self.parent
            except AssertionError:
                raise ImportError("Error: Failed to resolve module.")
        self._check_child() # Verify that the submethod is valid
        return import_module(self.parent) # Return it as inst object

    def _is_numpy(self):
        try:
            assert self.parent != "numpy.random"
            return False
        except AssertionError:
            return True

    def _check_child(self):
        try:
            getattr(self.parent, self.method) # Check if parent contains child
        except:
            ImportError("Error: module %s not in %s" %(self.method, self.parent))