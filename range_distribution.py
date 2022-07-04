import random
import numpy

def get_uniform_range_distribution(lim_a, lim_b, number_of_points):

    return numpy.linspace(lim_a, lim_b, number_of_points).tolist()

def get_random_range_distribution(lim_a, lim_b, number_of_points):

    numbers = []

    for x in range(number_of_points):

        numbers.append(random.uniform(lim_a, lim_b))

    return numbers