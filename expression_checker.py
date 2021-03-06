import os
from errors import *

# Chequeador de la sintaxis de la expresion matematica
def expression_checker(expression_string):

    file = open('cache\\function_checker.py', 'w')

    file.write('from math import *\n\n\ndef function_checker(x):\n\n\ttry:\n\n\t\t' + expression_string + '\n\n\texcept:\n\n\t\tpass\n\n\nfunction_checker(0)')

    file.close()

    if os.system('python cache\\function_checker.py') != 0:

        syntax_error()

    os.system('erase cache\\function_checker.py')

    return True