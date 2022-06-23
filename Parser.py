def Parse(cad):

    file = open('function.py', 'w')

    #Try to set NameError

    file.write('from math import *\n\ndef func(x):\n\n\ttry:\n\n\t\treturn (' + cad + ', 0)\n\n\texcept:\n\n\t\treturn (0, -1)')

    file.close()