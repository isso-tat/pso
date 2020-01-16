import random


def randomType():
    if random.random() > 0.5:
        return 0
    else:
        return 1


def randomFloat():
    return random.uniform(-1, 1)


class AbcAgent:
    type = 0
    max_val = 0
    min_val = 0
    dimension = 0
    counter = 0
    position = []
    candidate = []
    h = None

    def __init__(self, dimension, max_val, min_val):
        self.type = randomType()
        self.max_val = max_val
        self.min_val = min_val
        self.dimension = dimension
        self.counter = 0
        self.position = []
        self.candidate = []
        self.h = 10000
        for _ in range(dimension):
            self.position.append(random.uniform(min_val, max_val))

    def calcCandidate(self, compare):
        for i in range(self.dimension):
            p = self.position[i] + randomFloat() * (self.position[i] - compare[i])
            self.candidate.append(p)

    def update(self, before, after):
        if before < after:
            self.counter += 1
            self.h = before
        else:
            self.position = self.candidate
            self.counter = 0
            self.h = after
