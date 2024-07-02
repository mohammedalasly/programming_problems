import heapq


def min_cost_distribution(components, line_capacities):
    num_lines = len(line_capacities)
    line_workloads = [0] * num_lines
    total_cost = 0

    for weight, complexity, compatible_lines in components:
        if len(compatible_lines) == 1:
            line = next(iter(compatible_lines))
            if line_workloads[line] + weight + complexity <= line_capacities[line]:
                line_workloads[line] += weight + complexity
            else:
                return float("inf")
        else:
            min_heap = []
            for line in compatible_lines:
                if line_workloads[line] + weight + complexity <= line_capacities[line]:
                    heapq.heappush(
                        min_heap, (line_workloads[line] + weight + complexity, line)
                    )

            if not min_heap:
                return float("inf")

            _, best_line = heapq.heappop(min_heap)
            line_workloads[best_line] += weight + complexity
            total_cost += weight + complexity

    return total_cost


# Unit tests
components1 = [(10, 2, {0}), (5, 1, {0}), (8, 3, {0})]
line_capacities1 = [100]
components2 = [(10, 2, {0, 1}), (5, 1, {1}), (8, 3, {0})]
line_capacities2 = [20, 20]
components3 = [(15, 4, {0, 1}), (10, 2, {0, 1}), (5, 1, {0, 1})]
line_capacities3 = [20, 20]
components4 = [(10, 2, {0, 2}), (5, 1, {1, 3}), (8, 3, {2, 3}), (12, 4, {0, 1})]
line_capacities4 = [20, 20, 20, 20]

print(
    min_cost_distribution(components1, line_capacities1)
)  # Expected Output: 0  // actuall Output: 0
print(
    min_cost_distribution(components2, line_capacities2)
)  # Expected Output: 5  // actuall Output: inf
print(
    min_cost_distribution(components3, line_capacities3)
)  # Expected Output: 10 // actuall Output: 37
print(
    min_cost_distribution(components4, line_capacities4)
)  # Expected Output: 18 // actuall Output: inf
