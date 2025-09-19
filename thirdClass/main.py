from thirdClass.algorithms.hill_climbing import hill_climbing
from thirdClass.algorithms.simulated_annealing import simulated_annealing
from thirdClass.algorithms.genetic_algorithm import genetic_algorithm
from thirdClass.utils.config import NUM_RUNS

from analysis_utils import (
    count_unique_solutions,
    most_frequent_solutions,
    compute_std
)

import numpy as np

def main():
    results = {
        "Hill Climbing": {"values": [], "solutions": []},
        "Simulated Annealing": {"values": [], "solutions": []},
        "Genetic Algorithm": {"values": [], "solutions": []}
    }

    for _ in range(NUM_RUNS):
        hc_sol, hc_val, _ = hill_climbing()
        sa_sol, sa_val, _ = simulated_annealing()
        ga_sol, ga_val, _ = genetic_algorithm()

        results["Hill Climbing"]["values"].append(hc_val)
        results["Hill Climbing"]["solutions"].append(hc_sol)

        results["Simulated Annealing"]["values"].append(sa_val)
        results["Simulated Annealing"]["solutions"].append(sa_sol)

        results["Genetic Algorithm"]["values"].append(ga_val)
        results["Genetic Algorithm"]["solutions"].append(ga_sol)

    stats = {}
    for algo, data in results.items():
        vals = data["values"]
        sols = data["solutions"]

        stats[algo] = {
            "average": round(np.mean(vals), 2),
            "best": max(vals),
            "worst": min(vals),
            "std_dev": compute_std(vals),
            "unique_solutions": count_unique_solutions(sols),
        }

        most_common_sols, freq = most_frequent_solutions(sols)
        stats[algo]["most_frequent_solutions"] = most_common_sols
        stats[algo]["most_frequent_count"] = freq

    ranking = sorted(stats.items(), key=lambda x: x[1]["average"], reverse=True)

    print(f"\n=== Algorithm Performance Over {NUM_RUNS} Runs ===\n")
    for algo, data in stats.items():
        print(f"{algo}:")
        print(f"  ➤ Average Value: {data['average']}")
        print(f"  ➤ Best Value:    {data['best']}")
        print(f"  ➤ Worst Value:   {data['worst']}")
        print(f"  ➤ Std Dev:       {data['std_dev']}")
        print(f"  ➤ Unique Solutions: {data['unique_solutions']}")
        print(f"  ➤ Most Frequent Solution(s) (occurred {data['most_frequent_count']} times):")
        for sol in data["most_frequent_solutions"]:
            print(f"     {sol}")
        print()

    print("=== Ranking by Average Value ===")
    for i, (algo, data) in enumerate(ranking, 1):
        print(f"{i}. {algo} (Average: {data['average']})")

if __name__ == "__main__":
    main()
