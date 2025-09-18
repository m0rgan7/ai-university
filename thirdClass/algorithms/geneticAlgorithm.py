import random
from utils.knapsack_utils import generate_random_solution, fitness, repair, total_weight

def crossover(p1, p2):
    point = random.randint(1, len(p1) - 1)
    c1 = repair(p1[:point] + p2[point:])
    c2 = repair(p2[:point] + p1[point:])
    return c1, c2

def mutation(individual, mutation_prob=0.02):
    mutated = individual[:]
    for i in range(len(mutated)):
        if random.random() < mutation_prob:
            mutated[i] = 1 - mutated[i]
    return repair(mutated)

def tournament(population, k=3):
    candidates = random.sample(population, k)
    return max(candidates, key=fitness)

def genetic_algorithm():
    population_size = 50
    generations = 120
    crossover_prob = 0.9
    mutation_prob = 0.02
    elite = 2

    population = [generate_random_solution() for _ in range(population_size)]

    for _ in range(generations):
        new_population = sorted(population, key=fitness, reverse=True)[:elite]
        while len(new_population) < population_size:
            p1 = tournament(population)
            p2 = tournament(population)
            if random.random() < crossover_prob:
                c1, c2 = crossover(p1, p2)
            else:
                c1, c2 = p1, p2
            new_population.append(mutation(c1, mutation_prob))
            if len(new_population) < population_size:
                new_population.append(mutation(c2, mutation_prob))
        population = new_population

    best = max(population, key=fitness)
    return best, fitness(best), total_weight(best)
