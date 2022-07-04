import matplotlib.pyplot as pyplot
from evaluate import *
from range_distribution import *

# Elimina los Nones de las listas
def delete_nones(list_a, list_b):

    assert(len(list_a) == len(list_b))

    temp_a = []
    temp_b = []

    list = []

    for i in range(len(list_a)):

        if list_a[i] != None and list_b[i] != None:

            temp_a.append(list_a[i])
            temp_b.append(list_b[i])
        
        elif len(temp_a) > 0 or len(temp_b) > 0:

            list.append((temp_a, temp_b))
            temp_a = []
            temp_b = []

    if len(temp_a) > 0 or len(temp_b) > 0:

        list.append((temp_a, temp_b))
        temp_a = []
        temp_b = []

    return list

# Imprime la funcion usando matplotlib
def plot_function(func, funcString, a, b, limA, limB, value, print_lim_a, print_lim_b, number_of_points):

    assert(a <= b)
    assert(limA <= limB)

    pyplot.grid()
    pyplot.axhline(0, color = "gray")
    pyplot.axvline(0, color = "gray")
    pyplot.xlim(a, b)

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

    coordinatesX = get_uniform_range_distribution(a, b, number_of_points)
    coordinatesY = evaluate_function_list(func, coordinatesX)

    coordinatesList = delete_nones(coordinatesX, coordinatesY)

    for coordinatesXAndY in coordinatesList:

        coordinatesX = coordinatesXAndY[0]
        coordinatesY = coordinatesXAndY[1]

        integralLimits = [(limA <= x and x <= limB) for x in coordinatesX]

        blue = [y > 0 for y in coordinatesY]
        red = [y < 0 for y in coordinatesY]

        for i in range(len(integralLimits)):

            blue[i] = blue[i] and integralLimits[i]
            red[i] = red[i] and integralLimits[i]

        pyplot.fill_between(coordinatesX, coordinatesY, facecolor = "lightskyblue", where = blue)
        pyplot.fill_between(coordinatesX, coordinatesY, facecolor = "lightpink", where = red)

        pyplot.plot(coordinatesX, coordinatesY, color = 'royalblue') 
        

    for coordinatesXAndY in coordinatesList:
       
        coordinatesX = coordinatesXAndY[0]

        flag = False

        for i in range(len(coordinatesX)):

            if limA <= coordinatesX[i] and coordinatesX[i] <= limB:

                pyplot.plot([coordinatesX[i], coordinatesX[i]], [0, func(coordinatesX[i])], color = "black")

                flag = True

                break

        if flag:

            break
            
    
    for coordinatesXAndY in reversed(coordinatesList):

        coordinatesX = coordinatesXAndY[0]

        flag = False

        for i in reversed(range(len(coordinatesX))):

            if limA <= coordinatesX[i] and coordinatesX[i] <= limB:

                pyplot.plot([coordinatesX[i], coordinatesX[i]], [0, func(coordinatesX[i])], color = "black")

                flag = True

                break

        if flag:

            break


    pyplot.show()