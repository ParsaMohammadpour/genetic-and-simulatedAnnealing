import numpy as np

from Gate import Gate
from Genetic import Genetic
from SE import SE


def get_input():
    lines = np.loadtxt("database.cnf", dtype=int, delimiter="  ", unpack=False)
    input = []
    gates = []

    for i in np.nditer(lines):
        if i == 0:
            gates.append(Gate(input[0], input[1], input[2]))
            input.clear()
        else:
            input.append(i)
    return gates

genetic = Genetic(get_input())
genetic.run()
#se = SE(get_input())
#se.run()