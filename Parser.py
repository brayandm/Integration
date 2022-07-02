def parse(expression_string):

    file = open('Function.py', 'w')

    file.write('from math import *\n\ndef function(x):\n\n\ttry:\n\n\t\treturn (' + expression_string + ', 0)\n\n\texcept NameError:\n\n\t\tfile = open(\'Cache\\\\NameError.txt\', \'w\')\n\n\t\tfile.write(\'True\')\n\n\t\tfile.close()\n\n\t\treturn (0, -1)\n\n\texcept:\n\n\t\treturn (0, -1)')

    file.close()