from random import randint
from numpy.random import rand
from math import exp

import matplotlib.pyplot as plt
import numpy as np


class SE:
    def __init__(self, gates):
        self.gates = gates
        self.pop = []

    def run(self):
        objs = []
        while True:
            print('new random population.')
            node = self.random_start()
            for i in range(50):
                neighbors = self.make_neighbor(node)
                objective = [self.objective_function(x) for x in neighbors]
                if max(objective) == len(self.gates):
                    print('hack result:')
                    for j in neighbors:
                        if len(self.gates) == self.objective_function(j):
                            print(j)
                            return
                node = self.change_neighbor(node, neighbors, i)
                objs.append(self.objective_function(node))
                ypoints = np.array(objs)
                xpoints = np.array([x for x in range(len(objs))])
                plt.plot(xpoints, ypoints, 'o:r')
                plt.show()
                print(f'node objective: {self.objective_function(node)}')

    def objective_function(self, array):
        counter = 0
        for i in self.gates:
            if i.gate_result(array):
                counter += 1
        return counter

    def random_start(self):
        return [randint(0, 1) for x in range(100)]

    def make_neighbor(self, node):
        neighbors = []
        objective = self.objective_function(node)
        counter = objective * 3
        while len(neighbors) < 1000 and counter > 0:
            array = node.copy()
            for i in self.gates:
                if not i.gate_result(array):
                    rnd = randint(0, 2)
                    if rnd == 0:
                        array[i.a] = 0 if array[i.a] == 1 else 1
                    elif rnd == 1:
                        array[i.b] = 0 if array[i.b] == 1 else 1
                    else:
                        array[i.c] = 0 if array[i.c] == 1 else 1
            neighbors.append(array)
            counter -= 1
        while len(neighbors) < 1000:
            array = node.copy()
            for i in range(objective):
                rnd = randint(0, 99)
                array[rnd] = 1 if array[rnd] == 0 else 0
            neighbors.append(array)
        return neighbors

    def change_neighbor(self, node, neighbors, i):
        max_objective = max([self.objective_function(x) for x in neighbors])
        node_objective = self.objective_function(node)
        metropolis = exp(-abs(max_objective - node_objective) / ((501 - i) / float(i + 1)))
        if max_objective - node_objective < 0 or rand() < metropolis:
            for i in neighbors:
                if self.objective_function(i) == max_objective:
                    return i
        return node