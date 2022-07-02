from evaluate import evaluate_function_in_range
import math

def rectangle_rule(function, lim_a, lim_b, iterations):

    result = 0

    height = (lim_b - lim_a) / iterations

    coordinates = evaluate_function_in_range(function, lim_a, lim_b, iterations*2 + 1)

    for it in range(iterations):

        value = coordinates[1][it*2 + 1]

        if value != None:

            result += value
            
    result *= height

    return result

def trapezoidal_rule(function, lim_a, lim_b, iterations):

    result = 0

    height = (lim_b - lim_a) / iterations

    coordinates = evaluate_function_in_range(function, lim_a, lim_b, iterations + 1)

    for it in range(iterations):

        value_a = coordinates[1][it]
        value_b = coordinates[1][it+1]

        if value_a != None and value_b != None:

            result += (value_a + value_b) / 2
            
    result *= height

    return result