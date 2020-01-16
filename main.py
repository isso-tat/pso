from psoagent import PsoAgent
from abcagent import AbcAgent
from agent_repository import AgentRepository
from functions.installer import FunctionInstaller
import matplotlib.pyplot as plt
import random
import time

dimension = 2
agentsCount = 20
maxIndex = 5000


def plot_figure(x, y):
    plt.plot(x, y)
    ax = plt.gca()
    ax.set_yscale('log')
    plt.title('results ' + functionClient.name)
    plt.xlabel('Steps', fontsize=18)
    plt.ylabel('Hulistics', fontsize=18)
    plt.show()


functionClient = FunctionInstaller().function_install(dimension)
valueMax = functionClient.maxVal
valueMin = functionClient.minVal


# PSO
def map_pso_agents():
    tmp_agents = []
    for _ in range(agentsCount):
        tmp_agent = PsoAgent(dimension, valueMin, valueMax)
        tmp_agents.append(tmp_agent)
        return tmp_agents


def do_pso():
    pso_agents = map_pso_agents()

    i = 0
    all_best_p = []
    all_best_h = None
    fig_x = []
    fig_y = []
    chunk = 100
    continueNext = True
    while continueNext:
        for agent in pso_agents:
            h = functionClient.hulistic(agent.position)
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


# comment out if you skip pso
do_pso()


# ABC
def map_abc_agents():
    tmp_agents = []
    for _ in range(agentsCount):
        tmp_agent = AbcAgent(dimension, valueMin, valueMax)
        tmp_agents.append(tmp_agent)
    return tmp_agents


abc_agent_repo = AgentRepository(map_abc_agents())


def calc_harvests():
    harvest_agents = [a for a in abc_agent_repo.agents if a.type == 0]
    for harvest_agent in harvest_agents:
        compare = abc_agent_repo.random_agent()
        harvest_agent.calcCandidate(compare.position)
        before = functionClient.hulistic(harvest_agent.position)
        after = functionClient.hulistic(harvest_agent.candidate)
        harvest_agent.update(before, after)


def calc_follow():
    follow_agents = [a for a in abc_agent_repo.agents if a.type == 1]
    for follow_agent in follow_agents:
        compare = abc_agent_repo.return_followed()
        follow_agent.calcCandidate(compare.position)
        before = functionClient.hulistic(follow_agent.position)
        after = functionClient.hulistic(follow_agent.candidate)
        follow_agent.update(before, after)


def delete_expired():
    deleted = abc_agent_repo.delete_expired()
    for _ in range(deleted):
        abc_agent = AbcAgent(dimension, valueMin, valueMax)
        abc_agent_repo.add_agent(abc_agent)


def do_abc():
    i = 0
    best_h = None
    best_p = None
    fig_x = []
    fig_y = []
    chunk = 100
    continueNext = True
    while continueNext:
        calc_harvests()
        calc_follow()
        delete_expired()

        best = abc_agent_repo.return_best()
        if best_h is None or best_h > best.h:
            best_h = best.h
            best_p = best.position

        if i % chunk is 0:
            fig_x.append(i)
            fig_y.append(best_h)
        i += 1
        if i > maxIndex:
            continueNext = False
    print(best_h, best_p)
    plot_figure(fig_x, fig_y)


# comment out if you skip this
do_abc()
