import os

def expression_checker(expression_string):

    file = open('cache\\function_checker.py', 'w')

    file.write('from math import *\n\n\ndef function_checker(x):\n\n\ttry:\n\n\t\t' + expression_string + '\n\n\texcept:\n\n\t\tpass\n\n\nfunction_checker(0)')

    file.close()

    flag = os.system('python cache\\function_checker.py') == 0

    os.system('erase cache\\function_checker.py')

    return flag