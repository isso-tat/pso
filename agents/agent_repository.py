from heapq import nsmallest
import random

countThreshold = 10


class AgentRepository:
    agents = []

    def __init__(self, agents):
        self.agents = agents

    def random_agent(self):
        return random.choice(self.agents)

    def return_followed(self):
        # At the beginning limit the number of candidate so that the better agents tend to be returned.
        count = random.randint(1, len(self.agents))
        good_agents = nsmallest(count, self.agents, key=lambda e: e.h)
        return random.choice(good_agents)

    def return_best(self):
        return nsmallest(1, self.agents, key=lambda e: e.h)[0]

    def add_agent(self, agent):
        self.agents.append(agent)

    def delete_expired(self):
        deleted = [a for a in self.agents if a.counter > countThreshold]
        count = 0
        for d in deleted:
            count += 1
            self.agents.remove(d)
        return count

