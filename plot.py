import matplotlib.pyplot as pyplot
from evaluate import *
from range_distribution import *

def delete_nones(list_a, list_b):

    assert(len(list_a) == len(list_b))

    list = []

    for i in range(len(list_a)):

        if list_a[i] != None and list_b[i] != None:

            list.append((list_a[i], list_b[i]))

    list_a.clear()
    list_b.clear()

    for x in list:

        list_a.append(x[0])
        list_b.append(x[1])

def plot_function(func, funcString, a, b, limA, limB, value, print_lim_a, print_lim_b, number_of_points):

    assert(a <= b)
    assert(limA <= limB)

    coordinates_x = get_uniform_range_distribution(a, b, number_of_points)
    coordinates = evaluate_function_in_range(func, coordinates_x)
    (coordinatesX, coordinatesY) = coordinates

    delete_nones(coordinatesX, coordinatesY)

    integralLimits = [(limA <= x and x <= limB) for x in coordinatesX]

    blue = [y > 0 for y in coordinatesY]
    red = [y < 0 for y in coordinatesY]

    for i in range(len(integralLimits)):

        blue[i] = blue[i] and integralLimits[i]
        red[i] = red[i] and integralLimits[i]

    pyplot.fill_between(coordinatesX, coordinatesY, facecolor = "lightskyblue", where = blue)
    pyplot.fill_between(coordinatesX, coordinatesY, facecolor = "lightpink", where = red)

    if float(print_lim_a) == float('-inf') and float(print_lim_b) == float('inf'):
    
        if(float(value) == float('inf')):

            pyplot.title(r'$\int_{-\infty}^{\infty}%s=\infty$' % (str(funcString)))
        
        elif(float(value) == float('-inf')):
            
            pyplot.title(r'$\int_{-\infty}^{\infty}%s=-\infty$' % (str(funcString)))

        else:

            pyplot.title(r'$\int_{-\infty}^{\infty}%s=%.5f$' % (str(funcString), float(value)))

    elif float(print_lim_a) == float('-inf'):
    
        if(float(value) == float('inf')):

            pyplot.title(r'$\int_{-\infty}^{%.2f}%s=\infty$' % (float(print_lim_b), str(funcString)))
        
        elif(float(value) == float('-inf')):
            
            pyplot.title(r'$\int_{-\infty}^{%.2f}%s=-\infty$' % (float(print_lim_b), str(funcString)))

        else:

            pyplot.title(r'$\int_{-\infty}^{%.2f}%s=%.5f$' % (float(print_lim_b), str(funcString), float(value)))

    elif float(print_lim_b) == float('inf'):

        if(float(value) == float('inf')):

            pyplot.title(r'$\int_{%.2f}^{\infty}%s=\infty$' % (float(print_lim_a), str(funcString)))
        
        elif(float(value) == float('-inf')):
            
            pyplot.title(r'$\int_{%.2f}^{\infty}%s=-\infty$' % (float(print_lim_a), str(funcString)))

        else:

            pyplot.title(r'$\int_{%.2f}^{\infty}%s=%.5f$' % (float(print_lim_a), str(funcString), float(value)))

    else:

        if(float(value) == float('inf')):

            pyplot.title(r'$\int_{%.2f}^{%.2f}%s=\infty$' % (float(print_lim_a), float(print_lim_b), str(funcString)))
        
        elif(float(value) == float('-inf')):
            
            pyplot.title(r'$\int_{%.2f}^{%.2f}%s=-\infty$' % (float(print_lim_a), float(print_lim_b), str(funcString)))

        else:

            pyplot.title(r'$\int_{%.2f}^{%.2f}%s=%.5f$' % (float(print_lim_a), float(print_lim_b), str(funcString), float(value)))

    pyplot.plot(coordinatesX, coordinatesY) 
    pyplot.grid()
    pyplot.axhline(0, color = "gray")
    pyplot.axvline(0, color = "gray")
    pyplot.xlim(a, b)

    for i in range(len(coordinatesX)):

        if limA <= coordinatesX[i] and coordinatesX[i] <= limB:

            pyplot.plot([coordinatesX[i], coordinatesX[i]], [0, func(coordinatesX[i])], color = "black")

            break
            

    for i in reversed(range(len(coordinatesX))):

        if limA <= coordinatesX[i] and coordinatesX[i] <= limB:

            pyplot.plot([coordinatesX[i], coordinatesX[i]], [0, func(coordinatesX[i])], color = "black")

            break


    pyplot.show()