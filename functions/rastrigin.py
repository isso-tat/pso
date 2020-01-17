from math import cos, pi


class Rastrigin:
    dimension = 0
    name = "Rastrigin"
    maxVal = 5
    minVal = -5

    def __init__(self, dimension):
        self.dimension = dimension

    def hulistic(self, position):
        h = 0
        h += 10 * self.dimension
        for i in range(self.dimension):
            h += position[i] * position[i] - 10 * cos(2 * pi * position[i])
        return h

