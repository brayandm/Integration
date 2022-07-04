from math import *

from errors import *

def function(x):

	x = float(x)

	try:

		return x

	except OverflowError:

		return float(0)

	except NameError:

		name_error()

		return None

	except:

		return None