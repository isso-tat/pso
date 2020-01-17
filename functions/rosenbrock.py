class Rosenbrock:
    dimension = 0
    name = "Rosenbrock"
    maxVal = 10
    minVal = -5

    def __init__(self, dimension):
        self.dimension = dimension

    def hulistic(self, position):
        h = 0
        for i in range(self.dimension - 1):
            h += 100*(position[i+1] - position[i]**2)**2
            h += (1 - position[i])**2
        return h
