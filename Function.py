from math import *

def function(x):

	try:

		return (x, 0)

	except NameError:

		file = open('Cache\\NameError.txt', 'w')

		file.write('True')

		file.close()

		return (0, -1)

	except:

		return (0, -1)