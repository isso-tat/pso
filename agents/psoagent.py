import random


class PsoAgent:
    past_best_p = []
    past_best_h = None
    selfC = 1
    allC = 1
    velocityC = 0.5
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
        for _ in range(dimension):
            self.position.append(random.uniform(min_val, max_val))
            self.velocity.append(random.uniform(min_val, max_val))

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
            p = self.position[i] + v
            if self.min_val > p:
                position.append(self.min_val)
            elif self.max_val < p:
                position.append(self.max_val)
            else:
                position.append(p)

        self.velocity = velocity
        self.position = position

    @staticmethod
    def randomFloat():
        return random.random()
