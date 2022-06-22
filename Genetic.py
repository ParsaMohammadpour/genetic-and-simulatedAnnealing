from random import randint

import matplotlib.pyplot as plt
import numpy as np

class Genetic:
    def __init__(self, gates):
        self.gates = gates
        self.pop = []

    def run(self):
        objs = []
        while True:
            print('new random population.')
            self.make_pop()
            for i in range(500):
                objs.append(sum([self.fitness_function(x) for x in self.pop]) / len(self.pop))
                ypoints = np.array(objs)
                xpoints = np.array([x for x in range(len(objs))])
                plt.plot(xpoints, ypoints, 'o:r')
                plt.show()
                print(f'step {i}')
                new_pop = self.pop + self.reproduction()
                max_fittness = max([self.fitness_function(x) for x in new_pop])
                print(f'new best fitness: {max_fittness}')
                if max_fittness == len(self.gates):
                    print('hack result:')
                    for j in new_pop:
                        if max_fittness == self.fitness_function(j):
                            print(j)
                            return
                fitness = self.make_fitness_array_for_rulles(new_pop)
                self.pop = self.ruller(out_len=100, main_list=new_pop,probability_list=fitness)

    def fitness_function(self, array):
        counter = 0
        for i in self.gates:
            if i.gate_result(array):
                counter += 1
        return counter

    def make_pop(self):
        self.pop.clear()
        for i in range(100):
            self.pop.append([randint(0, 1) for x in range(100)])

    def reproduction(self):
        fitness = self.make_fitness_array_for_rulles(self.pop)
        child = self.ruller(out_len=1000, main_list=self.pop,probability_list=fitness)
        return [self.mutation(x) for x in child]

    def mutation(self, child):
        for i in self.gates:
            if not i.gate_result(child):
                rnd = randint(0, 2)
                if rnd == 0:
                    child[i.a] = 0 if child[i.a] == 1 else 1
                elif rnd == 1:
                    child[i.b] = 0 if child[i.b] == 1 else 1
                else:
                    child[i.c] = 0 if child[i.c] == 1 else 1
        return child

    def make_fitness_array_for_rulles(self, pop):
        fitness = [self.fitness_function(x) for x in pop]
        min_fitness = min(fitness)
        return [x - min_fitness for x in fitness]

    def ruller(self, out_len, main_list, probability_list):
        out = []
        sum_fitness = sum(probability_list)
        for i in range(out_len):
            rnd = randint(0, sum_fitness)
            counter = 0
            while counter < main_list.__len__() and probability_list[counter] < rnd:
                rnd -= probability_list[counter]
                counter += 1
            out.append(main_list[counter].copy())
        return out