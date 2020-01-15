import random


class Agent:
    past_best_p = []
    past_best_h = None
    selfC = 1
    allC = 1
    velocityC = 1
    velocity = []
    position = []
    max_val = 0
    min_val = 0
    dimension = 0

    def __init__(self, dimension, min_val, max_val):
        self.dimension = dimension
        self.max_val = max_val
        self.min_val = min_val
        self.position = []
        self.velocity = []
        for i in range(dimension):
            self.position.append(random.uniform(min_val, max_val))
            self.velocity.append(random.uniform(min_val, max_val))
        # print(len(self.position))

    def check_best(self, h):
        if self.past_best_h is None or h < self.past_best_h:
            self.past_best_p = self.position
            self.past_best_h = h

    def update(self, all_best):
        velocity = []
        position = []
        for i in range(self.dimension):
            v = self.velocityC*self.velocity[i]
            v += self.selfC*random.random()*(self.past_best_p[i] - self.position[i])
            v += self.allC*random.random()*(all_best[i] - self.position[i])
            velocity.append(v)
            position.append(self.position[i] + v)
        self.velocity = velocity
        self.position = position

    @staticmethod
    def randomFloat():
        return random.random()
