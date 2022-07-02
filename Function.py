from math import *

from errors import *

def function(x):

	try:

		return x

	except NameError:

		name_error()

		return None

	except:

		return None