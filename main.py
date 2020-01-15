from agent import Agent
from functions.installer import FunctionInstaller
import time

# PSO

dimension = 2
valueMax = 5
valueMin = -5
agents = []
agentsCount = 10

functionClient = FunctionInstaller().function_install(dimension)

for i in range(agentsCount):
    agent = Agent(2, valueMin, valueMax)
    agents.append(agent)

maxIndex = 100
i = 0
all_best_p = []
all_best_h = None
continueNext = True
while continueNext:
    for agent in agents:
        h = functionClient.hulistic(agent)
        agent.check_best(h)
        if len(all_best_p) is 0:
            all_best_p = agent.position
        if all_best_h is None or all_best_h > h:
            all_best_p = agent.position
            all_best_h = h
        agent.update(all_best_p)
    i += 1
    if i > maxIndex:
        continueNext = False
print(all_best_h, all_best_p)


# ABC
print("")
