from math import *

from errors import *

def function(x):

	try:

		return (x, 0)

	except NameError:

		name_error()

		return (0, -1)

	except:

		return (0, -1)