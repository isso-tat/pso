class Sphere:
    dimension = 0

    def __init__(self, dimension):
        self.dimension = dimension

    def hulistic(self, agent):
        h = 0
        for i in range(self.dimension):
            h += agent.position[i]*agent.position[i]
        return h

