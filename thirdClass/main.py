from thirdClass.algorithms.hill_climbing import hill_climbing
from thirdClass.algorithms.simulated_annealing import simulated_annealing
from thirdClass.algorithms.genetic_algorithm import genetic_algorithm
from thirdClass.utils.knapsack_utils import total_weight
from thirdClass.utils.config import NUM_RUNS
import numpy as np

results = {
    "Hill Climbing": [],
    "Simulated Annealing": [],
    "Genetic Algorithm": []
}

for _ in range(NUM_RUNS):
    hc, val_hc, _ = hill_climbing()
    sa, val_sa, _ = simulated_annealing()
    ga, val_ga, _ = genetic_algorithm()

    results["Hill Climbing"].append(val_hc)
    results["Simulated Annealing"].append(val_sa)
    results["Genetic Algorithm"].append(val_ga)

stats = {}
for algo, vals in results.items():
    stats[algo] = {
        "average": round(np.mean(vals), 2),
        "best": max(vals),
        "worst": min(vals)
    }

ranking = sorted(stats.items(), key=lambda x: x[1]["average"], reverse=True)

print("\n=== Algorithm Performance Over", NUM_RUNS, "Runs ===\n")
for algo, data in stats.items():
    print(f"{algo}:")
    print(f"  ➤ Average Value: {data['average']}")
    print(f"  ➤ Best Value:    {data['best']}")
    print(f"  ➤ Worst Value:   {data['worst']}\n")

print("=== Ranking by Average Value ===")
for i, (algo, data) in enumerate(ranking, 1):
    print(f"{i}. {algo} (Average: {data['average']})")
