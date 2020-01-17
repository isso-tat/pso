from math import cos, sqrt


class Griewank:
    dimension = 0
    name = "Griewank"
    maxVal = 600
    minVal = -600

    def __init__(self, dimension):
        self.dimension = dimension

    def hulistic(self, position):
        h = 1
        arg1 = 0
        arg2 = 1
        for i in range(self.dimension):
            arg1 += position[i]**2
        arg1 /= 4000
        for i in range(self.dimension):
            arg2 *= cos(position[i]/sqrt(i+1))
        h = h + arg1 - arg2
        return h
