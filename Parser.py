def parse(expression_string):

    file = open('function.py', 'w')

    file.write('from math import *\n\nfrom errors import *\n\ndef function(x):\n\n\ttry:\n\n\t\treturn ' + expression_string + '\n\n\texcept NameError:\n\n\t\tname_error()\n\n\t\treturn None\n\n\texcept:\n\n\t\treturn None')

    file.close()