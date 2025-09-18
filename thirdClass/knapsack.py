import random
import numpy as np

items = [
    {"id": 1,  "value": 60,  "weight": 10},
    {"id": 2,  "value": 100, "weight": 20},
    {"id": 3,  "value": 120, "weight": 30},
    {"id": 4,  "value": 90,  "weight": 15},
    {"id": 5,  "value": 30,  "weight": 5},
    {"id": 6,  "value": 70,  "weight": 12},
    {"id": 7,  "value": 40,  "weight": 7},
    {"id": 8,  "value": 160, "weight": 25},
    {"id": 9,  "value": 20,  "weight": 3},
    {"id": 10, "value": 50,  "weight": 9},
    {"id": 11, "value": 110, "weight": 18},
    {"id": 12, "value": 85,  "weight": 14},
    {"id": 13, "value": 95,  "weight": 16},
    {"id": 14, "value": 200, "weight": 28},
    {"id": 15, "value": 55,  "weight": 6},
]

MAX_CAPACITY = 50

def fitness(solution):
    total_value = 0
    total_weight = 0
    for i, selected in enumerate(solution):
        if selected:
            total_value += items[i]["value"]
            total_weight += items[i]["weight"]
    if total_weight > MAX_CAPACITY:
        return 0
    return total_value

def total_weight(solution):
    return sum(items[i]["weight"] for i in range(len(solution)) if solution[i])

def generate_random_solution():
    solution = [random.randint(0, 1) for _ in range(len(items))]
    return repair(solution)

def repair(solution):
    while total_weight(solution) > MAX_CAPACITY:
        idxs = [i for i in range(len(solution)) if solution[i]]
        solution[random.choice(idxs)] = 0
    return solution

def neighbors(solution):
    neigh = []
    for i in range(len(solution)):
        neighbor = solution[:]
        neighbor[i] = 1 - neighbor[i]
        neigh.append(repair(neighbor))
    return neigh

def hill_climbing():
    current = generate_random_solution()
    best_fitness = fitness(current)
    iterations = 0
    while iterations < 300:
        best_neighbor = current
        for n in neighbors(current):
            if fitness(n) > best_fitness:
                best_neighbor = n
                best_fitness = fitness(n)
        if best_neighbor == current:
            break
        current = best_neighbor
        iterations += 1
    return current, fitness(current), total_weight(current)

def simulated_annealing():
    T = 50.0
    Tmin = 0.1
    alpha = 0.95
    steps_per_T = 30

    current = generate_random_solution()
    best = current[:]
    best_value = fitness(current)

    while T > Tmin:
        for _ in range(steps_per_T):
            neighbor = current[:]
            idx = random.randint(0, len(neighbor) - 1)
            neighbor[idx] = 1 - neighbor[idx]
            neighbor = repair(neighbor)

            delta = fitness(neighbor) - fitness(current)

            if delta > 0 or random.uniform(0, 1) < np.exp(delta / T):
                current = neighbor
                if fitness(current) > best_value:
                    best = current[:]
                    best_value = fitness(current)
        T *= alpha
    return best, fitness(best), total_weight(best)

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

hc, hc_value, hc_weight = hill_climbing()
sa, sa_value, sa_weight = simulated_annealing()
ga, ga_value, ga_weight = genetic_algorithm()

print("=== Hill Climbing ===")
print("Items:", [i+1 for i in range(len(hc)) if hc[i]])
print("Value:", hc_value, "| Weight:", hc_weight)

print("\n=== Simulated Annealing ===")
print("Items:", [i+1 for i in range(len(sa)) if sa[i]])
print("Value:", sa_value, "| Weight:", sa_weight)

print("\n=== Genetic Algorithm ===")
print("Items:", [i+1 for i in range(len(ga)) if ga[i]])
print("Value:", ga_value, "| Weight:", ga_weight)
