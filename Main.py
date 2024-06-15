import numpy as np
import random
import tkinter as tk
from tkinter import messagebox

# Genetic Algorithm Functions
def generate_population(pop_size, puzzle):
    population = []
    for _ in range(pop_size):
        individual = puzzle.copy()
        for i in range(9):
            missing = list(set(range(1, 10)) - set(individual[i]))
            np.random.shuffle(missing)
            individual[i] = [x if x != 0 else missing.pop() for x in individual[i]]
        population.append(individual)
    return population



## new changes

#test Lotfi
#hi