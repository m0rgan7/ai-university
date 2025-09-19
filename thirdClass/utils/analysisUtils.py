from collections import Counter
import numpy as np

def count_unique_solutions(solutions):
    return len(set(tuple(sol) for sol in solutions))

def most_frequent_solutions(solutions):
    counted = Counter(tuple(sol) for sol in solutions)
    max_freq = max(counted.values())
    most_common = [list(sol) for sol, freq in counted.items() if freq == max_freq]
    return most_common, max_freq

def compute_std(values):
    return round(np.std(values), 2)
