# Creando error de sintaxis
def syntax_error():
    
    file = open('cache\\SyntaxError.txt', 'w')

    file.close()

# Creando error de nombre
def name_error():
    
    file = open('cache\\NameError.txt', 'w')

    file.close()

# Creando error de integracion
def integration_error():

    file = open('cache\\IntegrationError.txt', 'w')

    file.close()

# Creando error de infinito
def infinity_error():

    file = open('cache\\InfinityError.txt', 'w')

    file.close()

# Chequeando error de sintaxis
def check_syntax_error():

    try:

        file = open('cache\\SyntaxError.txt', 'r')

        file.close()

        return True
    
    except:

        return False

# Chequeando error de nombre
def check_name_error():
    
    try:

        file = open('cache\\NameError.txt', 'r')

        file.close()

        return True
    
    except:

        return False

# Chequeando error de integracion
def check_integration_error():

    try:

        file = open('cache\\IntegrationError.txt', 'r')

        file.close()

        return True
    
    except:

        return False

# Chequeando error de infinito
def check_infinity_error():

    try:

        file = open('cache\\InfinityError.txt', 'r')

        file.close()

        return True
    
    except:

        return False