from evaluate import *
from range_distribution import *

def rectangle_rule(function, lim_a, lim_b, iterations):

    result = 0

    width = (lim_b - lim_a) / iterations

    coordinates_x = get_uniform_range_distribution(lim_a, lim_b, iterations * 2 + 1)
    coordinates = evaluate_function_in_range(function, coordinates_x)

    for it in range(iterations):

        value = coordinates[1][it * 2 + 1]

        if value != None:

            result += value
            
    result *= width

    return result

def trapezoidal_rule(function, lim_a, lim_b, iterations):

    result = 0

    width = (lim_b - lim_a) / iterations

    coordinates_x = get_uniform_range_distribution(lim_a, lim_b, iterations + 1)
    coordinates = evaluate_function_in_range(function, coordinates_x)

    for it in range(iterations):

        value_a = coordinates[1][it]
        value_b = coordinates[1][it+1]

        if value_a != None and value_b != None:

            result += (value_a + value_b) / 2
            
    result *= width

    return result

def simpson_rule(function, lim_a, lim_b, iterations):

    result = 0

    width = (lim_b - lim_a) / (2 * iterations)

    coordinates_x = get_uniform_range_distribution(lim_a, lim_b, iterations * 2 + 1)
    coordinates = evaluate_function_in_range(function, coordinates_x)

    for it in range(iterations):

        value_a = coordinates[1][it * 2]
        value_b = coordinates[1][(it + 1) * 2]

        if value_a != None and value_b != None:

            result += (value_a + 4 * coordinates[1][it * 2 + 1] + value_b)

    result *= width / 3

    return result

def monte_carlo_method(function, lim_a, lim_b, iterations):

    result = 0

    width = (lim_b - lim_a) / iterations

    coordinates_x = get_random_range_distribution(lim_a, lim_b, iterations)
    coordinates = evaluate_function_in_range(function, coordinates_x)

    for it in range(iterations):

        value = coordinates[1][it]

        if value != None:

            result += value

    result *= width

    return result

def adaptive_integration_method(function, lim_a, lim_b, iterations, relative_error, level = 1, level_limit = 5):

    value = simpson_rule(function, lim_a, lim_b, iterations)
    better_value = simpson_rule(function, lim_a, lim_b, iterations * 2)

    if level >= level_limit:

        return better_value

    if abs(better_value) == 0 or abs(value - better_value) / abs(better_value) < relative_error:

        return better_value

    middle = (lim_a + lim_b) / 2

    return adaptive_integration_method(function, lim_a, middle, iterations, relative_error, level + 1, level_limit) + adaptive_integration_method(function, middle, lim_b, iterations, relative_error, level + 1, level_limit)
