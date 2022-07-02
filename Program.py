from parser import *
from numerical_methods import *
from expression_checker import *
from errors import *
from clear_cache import *
from decorators import *

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

    print('\nInsert the limit A (float number or inf):\n')

    lim_a = input()

    if lim_a.lower() == 'inf':

        lim_a = None

        break

    try:

        lim_a = float(lim_a)

        break

    except:

        print('\nThe lim A is incorrect. Repeat it again\n')

while True:

    print('\nInsert the limit B (float number or inf):\n')

    lim_b = input()

    if lim_b.lower() == 'inf':

        lim_b = None

        break

    try:

        lim_b = float(lim_b)

        break

    except:

        print('\nThe lim B is incorrect. Repeat it again\n')

from function import *

if lim_a == None and lim_b == None:

    new_function = inf_to_inf(function, lim_a, lim_b)
    lim_a = -1
    lim_b = 1

elif lim_a == None:

    new_function = inf_to_float(function, lim_a, lim_b)
    lim_a = 0
    lim_b = 1

elif lim_b == None:

    new_function = float_to_inf(function, lim_a, lim_b)
    lim_a = 0
    lim_b = 1

else:

    new_function = function

print(new_function(0))
print(new_function(0.1))
print(new_function(0.2))
print(new_function(0.3))

val = simpson_rule(new_function, lim_a, lim_b, 10)

print('\nThe integral value is ' + str(val))


