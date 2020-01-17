class Minima2n:
    dimension = 0
    name = "2n Minima"
    maxVal = 5
    minVal = -5

    def __init__(self, dimension):
        self.dimension = dimension

    def hulistic(self, position):
        h = 0
        for p in position:
            h += p**4 - 16*p**2 + 5*p
        return h
