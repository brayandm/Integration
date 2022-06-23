from Parser import Parse
from NumericalMethods import RectangleRule

print('Insert the function:\n')

cad = input()

Parse(cad)

from Function import func

print('\nInsert the limit A:\n')

limA = input()

print('\nInsert the limit B:\n')

limB = input()

val = RectangleRule(func, float(limA), float(limB), 1000000)

print("\nThe integral value is: " + str(val))

input()

