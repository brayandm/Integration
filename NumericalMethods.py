def RectangleRule(func, limA, limB, iterations):

    result = 0

    height = (limB - limA) / iterations


    for it in range(iterations):

        value = func(limA + height * (it + 0.5))

        if value[1] == 0:

            result += value[0]
            

    result *= height

    return result