import numpy

def evaluate_function(function, x):

    try:

        y = function(x)

        if y[1] != 0:

            return None
        
        return float(y[0])

    except:

        return None


def evaluate_function_list(function, coordinates_x):

    coordinates_y = []

    for x in coordinates_x:

       coordinates_y.append(evaluate_function(function, x))

    for i in range(len(coordinates_y) - 1):

        if coordinates_y[i] == None and coordinates_y[i + 1] == None:

            file = open('Cache\\IntegrationError.txt', 'w')

            file.write('True')

            file.close()

    return coordinates_y


def evaluate_function_in_range(function, a, b, number_of_points):

    coordinates_x = numpy.linspace(a, b, number_of_points).tolist()
    coordinates_y = evaluate_function_list(function, coordinates_x)

    return (coordinates_x, coordinates_y)