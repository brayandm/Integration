from math import *

from errors import *

def function(x):

	try:

		return 0

	except NameError:

		name_error()

		return None

	except:

		return None