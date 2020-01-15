class Sphere:
    dimension = 0
    name = "Sphere"
    maxVal = 5
    minVal = -5

    def __init__(self, dimension):
        self.dimension = dimension

    def hulistic(self, agent):
        h = 0
        for i in range(self.dimension):
            h += agent.position[i]*agent.position[i]
        return h

