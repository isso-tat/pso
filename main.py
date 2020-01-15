from agent import Agent
from functions.installer import FunctionInstaller
import matplotlib.pyplot as plt


def plot_figure(x, y):
    plt.plot(x, y)
    ax = plt.gca()
    ax.set_yscale('log')
    plt.title('results ' + functionClient.name)
    plt.xlabel('Steps', fontsize=18)
    plt.ylabel('Hulistics', fontsize=18)
    plt.show()


# PSO

dimension = 2
agents = []
agentsCount = 5

functionClient = FunctionInstaller().function_install(dimension)
valueMax = functionClient.maxVal
valueMin = functionClient.minVal

for i in range(agentsCount):
    agent = Agent(2, valueMin, valueMax)
    agents.append(agent)

maxIndex = 1000
i = 0
all_best_p = []
all_best_h = None
fig_x = []
fig_y = []
chunk = 10
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
    if i % chunk is 0:
        fig_x.append(i)
        fig_y.append(all_best_h)
    i += 1
    if i > maxIndex:
        continueNext = False
print(all_best_h, all_best_p)
plot_figure(fig_x, fig_y)


# ABC

print("")



