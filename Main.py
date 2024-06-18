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


def fitness(individual):
    score = 0
    for i in range(9):
        row = individual[i]
        col = [individual[j][i] for j in range(9)]
        score += len(set(row)) + len(set(col))
    return score

def select(population, fitnesses):
    total_fitness = sum(fitnesses)
    probabilities = [f / total_fitness for f in fitnesses]
    return population[np.random.choice(range(len(population)), p=probabilities)]
    

def crossover(parent1, parent2):
    crossover_point = random.randint(0, 8)
    child = np.vstack((parent1[:crossover_point], parent2[crossover_point:]))
    return child
