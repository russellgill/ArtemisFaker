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

import matplotlib.pyplot as plt
import numpy as np
import random as rd
import pandas as pd
import math

def normalize(max, min, point):
    norm = (point - min) / (max - min)
    return norm

def binary(y_data: list, point: int, xdata: list):
    
    first = 0
    last = len(y_data) - 1
    
    while (first <= last):
        mid = (first + last) // 2
        if (point == y_data[mid]):
            return {xdata[mid] : y_data[mid]}
        else:
            if point < y_data[mid]:
                last = mid - 1
            else:
                first = mid + 1
                
    last = len(y_data) - 1
    found = False
    
    while not found:
        if (step + 1) < len(y_data):
            mid = (first + last) // 2
            if ((y_data[mid] < point) and (y_data[mid + 1] > point)):
                found = True
                return {xdata[mid] : y_data[mid], xdata[mid + 1] : y_data[mid + 1]}
            else:
                if point < y_data[mid]:
                    last = mid - 1
                else:
                    first = mid + 1
        else:
            raise IndexError("Iterations exceed total list size. \
                              Either the point does not exist, \
                              or the array is not normalized")

def interp(point: float, ui: float, uj: float, xi: float, xj: float) -> float:
    
    a = ((uj - point) / (uj - ui)) * xi
    b = ((point - ui) / (uj - ui)) * xj
    
    return a + b

def execute(self, sample_y, edges):
    found_x = []     
    for y in sample_y:
        result = binary(normed, y, edges[1:])
        found_x.append(result)

    i = 0
    interpolated = []
    for dicts in found_x:
        y_vals = []
        x_vals = []
        for x, y in dicts.items():
            x_vals.append(x)
            y_vals.append(y)
            # point: float, ui: float, uj: float, xi: float, xj: float
        result = interp(sample_y[i], y_vals[0], y_vals[1], x_vals[0], x_vals[1])
        interpolated.append(result)
        i += 1

    return np.histogram(interpolated)
