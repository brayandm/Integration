from math import *

from errors import *

def function(x):

	try:

		return e**x

	except NameError:

		name_error()

		return None

	except Exception as e:

		print(e)

		return None