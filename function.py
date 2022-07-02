from math import *

from errors import *

def function(x):

	x = float(x)

	try:

		return 3

	except OverflowError:

		return float('inf')

	except NameError:

		name_error()

		return None

	except:

		return None