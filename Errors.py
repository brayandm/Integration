def syntax_error():
    
    file = open('cache\\SyntaxError.txt', 'w')

    file.close()

def name_error():
    
    file = open('cache\\NameError.txt', 'w')

    file.close()

def integration_error():

    file = open('cache\\IntegrationError.txt', 'w')

    file.close()

def infinity_error():

    file = open('cache\\InfinityError.txt', 'w')

    file.close()

def check_syntax_error():

    try:

        file = open('cache\\SyntaxError.txt', 'r')

        file.close()

        return True
    
    except:

        return False

def check_name_error():
    
    try:

        file = open('cache\\NameError.txt', 'r')

        file.close()

        return True
    
    except:

        return False

def check_integration_error():

    try:

        file = open('cache\\IntegrationError.txt', 'r')

        file.close()

        return True
    
    except:

        return False

def check_infinity_error():

    try:

        file = open('cache\\InfinityError.txt', 'r')

        file.close()

        return True
    
    except:

        return False