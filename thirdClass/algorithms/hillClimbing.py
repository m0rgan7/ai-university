from utils.knapsack_utils import generate_random_solution, fitness, neighbors, total_weight

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
