from evaluate import evaluate_function_list
from expression_checker import *
from numerical_methods import *
from clear_cache import *
from decorators import *
from parser import *
from errors import *
from plot import *

ITERATIONS = 100000

while True:

    clear_cache()

    print('Insert the function:\n')

    cad = input()

    expression_checker(cad)

    if not check_syntax_error():

        break

    print('\nThe expression syntax is incorrect. Repeat it again\n')

parse(cad)

while True:

    while True:

        print('\nInsert the limit A (float number or -inf):\n')

        lim_a = input()

        try:

            lim_a = float(lim_a)

            assert(lim_a != float('inf'))

            break

        except:

            print('\nThe lim A is incorrect. Repeat it again\n')

    while True:

        print('\nInsert the limit B (float number or inf):\n')

        lim_b = input()

        try:

            lim_b = float(lim_b)

            assert(lim_b != float('-inf'))

            break

        except:

            print('\nThe lim B is incorrect. Repeat it again\n')

    from function import *

    if lim_a == float('-inf') and lim_b == float('inf'):

        new_function = inf_to_inf(function, lim_a, lim_b)
        new_lim_a = -1
        new_lim_b = 1

        break

    elif lim_a == float('-inf'):

        new_function = inf_to_float(function, lim_a, lim_b)
        new_lim_a = 0
        new_lim_b = 1

        break

    elif lim_b == float('inf'):

        new_function = float_to_inf(function, lim_a, lim_b)
        new_lim_a = 0
        new_lim_b = 1

        break

    else:

        if lim_a > lim_b:

            print('\nThe lim A must be less or equal than lim B. Repeat it again\n')

            continue

        new_function = function
        new_lim_a = lim_a
        new_lim_b = lim_b

        break

val = simpson_rule(new_function, new_lim_a, new_lim_b, ITERATIONS)

if check_name_error():

    print('\nThere is a variable name error, the variable name in the function must be \'x\'')

    exit(0)

if check_integration_error():

    print('\nThe function is not integrable in this interval')

    exit(0)

if lim_a == float('-inf') and lim_b == float('inf'):

    plot_function(function, cad, -100, 100, -100, 100, val, lim_a, lim_b, ITERATIONS)

elif lim_a == float('-inf'):

    plot_function(function, cad, lim_b - 10*abs(lim_b), lim_b + abs(lim_b), lim_b - 10*abs(lim_b), lim_b, val, lim_a, lim_b, ITERATIONS)

elif lim_b == float('inf'):

    plot_function(function, cad, lim_a - abs(lim_a), lim_a + 10*abs(lim_a), lim_a, lim_a + 10*abs(lim_a), val, lim_a, lim_b, ITERATIONS)

else:

    plot_function(new_function, cad, lim_a - (lim_b - lim_a) * 0.2, lim_b + (lim_b - lim_a) * 0.2, lim_a, lim_b, val, lim_a, lim_b, ITERATIONS)