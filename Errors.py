def syntax_error():
    
    file = open('Cache\\SyntaxError.txt', 'w')

    file.close()

def name_error():
    
    file = open('Cache\\NameError.txt', 'w')

    file.close()

def integration_error():

    file = open('Cache\\IntegrationError.txt', 'w')

    file.close()

def check_syntax_error():

    try:

        file = open('Cache\\SyntaxError.txt', 'r')

        file.close()

        return True
    
    except:

        return False

def check_name_error():
    
    try:

        file = open('Cache\\NameError.txt', 'r')

        file.close()

        return True
    
    except:

        return False

def check_integration_error():

    try:

        file = open('Cache\\IntegrationError.txt', 'r')

        file.close()

        return True
    
    except:

        return False