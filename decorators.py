# Esto es una funcion decoradora que sirve para tranformar una integral con 
# limites infinitos en una integral con limites finitos
def inf_to_inf(function, lim_a, lim_b):

    def new_function(x):

        value = function(x / (1 - x*x))

        if value == None:

            return None

        try:

            return value * (1 + x*x) / (1 - x*x) / (1 - x*x)

        except:

            return None

    return new_function

# Esto es una funcion decoradora que sirve para tranformar una integral con 
# limites infinitos en una integral con limites finitos
def inf_to_float(function, lim_a, lim_b):

    def new_function(x):

        value = function(lim_b - (1 - x) / x)

        if value == None:

            return None

        try:

            return value / (x) / (x)

        except:

            return None

    return new_function

# Esto es una funcion decoradora que sirve para tranformar una integral con 
# limites infinitos en una integral con limites finitos
def float_to_inf(function, lim_a, lim_b):

    def new_function(x):

        value = function(lim_a + x / (1 - x))

        if value == None:

            return None

        try:

            return value / (1 - x) / (1 - x)

        except:

            return None

    return new_function