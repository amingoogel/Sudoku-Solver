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


def mutate(individual, mutation_rate):
    for i in range(9):
        if random.random() < mutation_rate:
            swap_indices = random.sample(range(9), 2)
            individual[i][swap_indices[0]], individual[i][swap_indices[1]] = individual[i][swap_indices[1]], individual[i][swap_indices[0]]
    return individual

def genetic_algorithm(puzzle, pop_size=100, mutation_rate=0.1, generations=1000):
    population = generate_population(pop_size, puzzle)
    for generation in range(generations):
        fitnesses = [fitness(individual) for individual in population]
        if max(fitnesses) == 162:
            return population[fitnesses.index(max(fitnesses))]
        new_population = []
        for _ in range(pop_size // 2):
            parent1 = select(population, fitnesses)
            parent2 = select(population, fitnesses)
            child1 = crossover(parent1, parent2)
            child2 = crossover(parent2, parent1)
            new_population.extend([mutate(child1, mutation_rate), mutate(child2, mutation_rate)])
        population = new_population
    return population[fitnesses.index(max(fitnesses))]

    # CSP Solver Functions
def is_valid(board, row, col, num):
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False
    box_x, box_y = row // 3 * 3, col // 3 * 3
    for i in range(3):
        for j in range(3):
            if board[box_x + i][box_y + j] == num:
                return False
    return True