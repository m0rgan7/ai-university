import random

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

from utils.config import MAX_CAPACITY

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
        if not idxs:
            break
        solution[random.choice(idxs)] = 0
    return solution

def neighbors(solution):
    neigh = []
    for i in range(len(solution)):
        neighbor = solution[:]
        neighbor[i] = 1 - neighbor[i]
        neigh.append(repair(neighbor))
    return neigh
