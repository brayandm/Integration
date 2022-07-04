import numpy
from errors import *

# Evaluando en X
def evaluate_function(function, x):

    try:
        
        return float(function(x))

    except:

        return None

# Evaluando varias X
def evaluate_function_list(function, coordinates_x):

    coordinates_y = []

    for x in coordinates_x:

       coordinates_y.append(evaluate_function(function, x))

    for i in range(len(coordinates_y)):

        if coordinates_y[i] == float('-inf') or coordinates_y[i] == float('inf'):

            infinity_error()

    for i in range(len(coordinates_y) - 1):

        if coordinates_y[i] == None and coordinates_y[i + 1] == None:

            integration_error()

    return coordinates_y