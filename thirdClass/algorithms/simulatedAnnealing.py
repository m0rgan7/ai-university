import random
import numpy as np
from utils.knapsack_utils import generate_random_solution, fitness, repair, total_weight

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
