from math import sin


class Alpine:
    dimension = 0
    name = "Alpine"
    maxVal = 10
    minVal = -10

    def __init__(self, dimension):
        self.dimension = dimension

    def hulistic(self, position):
        h = 0
        for p in position:
            tmp = p*sin(p)
            tmp += 0.1*p
            if tmp < 0:
                tmp *= -1
            h += tmp
        return h
