from Parser import Parse
from NumericalMethods import RectangleRule
from Plot import *

print('Insert the function:\n')

cad = input()

Parse(cad)

from Function import func

print('\nInsert the limit A:\n')

limA = float(input())

print('\nInsert the limit B:\n')

limB = float(input())

val = RectangleRule(func, limA, limB, 1000000)

# print("\nThe integral value is: " + str(val))

# input()

PlotFunction(func, cad, limA - (limB-limA)*0.2, limB + (limB-limA)*0.2, limA, limB, val)

