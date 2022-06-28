import matplotlib.pyplot as pyplot
import numpy
import math

def EvalFunction(func, pointX):

    pointY = []

    for x in pointX:

        try:

            y = func(x)
            
            if type(y) == complex:

                pointY.append(None)
            
            else:

                pointY.append(y)

        except:

            pointY.append(None)

    return pointY


def DeleteNones(pointX, pointY):

    assert(len(pointX) == len(pointY))

    points = []

    for i in range(len(pointX)):

        if pointX[i] != None and pointY[i] != None:

            points.append((pointX[i], pointY[i]))

    pointX.clear()
    pointY.clear()

    for point in points:

        pointX.append(point[0])
        pointY.append(point[1])


def PlotFunction(func, funcString, a, b, limA, limB, value):

    assert(a <= b)
    assert(limA <= limB)

    granularity = 100000

    coordinatesX = numpy.linspace(a, b, granularity).tolist()
    coordinatesY = EvalFunction(func, coordinatesX)

    DeleteNones(coordinatesX, coordinatesY)

    integralLimits = [(limA <= x and x <= limB) for x in coordinatesX]
    
    blue = [y > 0 for y in coordinatesY]
    red = [y < 0 for y in coordinatesY]

    for i in range(len(integralLimits)):

        blue[i] = blue[i] and integralLimits[i]
        red[i] = red[i] and integralLimits[i]

    pyplot.fill_between(coordinatesX, coordinatesY, facecolor = "lightskyblue", where = blue)
    pyplot.fill_between(coordinatesX, coordinatesY, facecolor = "lightpink", where = red)
    pyplot.title(r'$\int_{%.2f}^{%.2f}%s=%.2f$' % (float(limA), float(limB), str(funcString), float(value)))
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