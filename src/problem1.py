class AssemblyLineOptimizer:
    def __init__(self, components, line_capacities):
        self.components = components
        self.line_capacities = line_capacities
        self.num_lines = len(line_capacities)
        self.line_workloads = [0] * self.num_lines
        self.total_cost = 0

    def calculate_cost(self, component, line):
        weight, complexity, _ = component
        return weight * complexity

    def distribute_components(self):
        for component in self.components:
            min_cost = float("inf")
            best_line = -1
            for line in component[2]:
                if (
                    self.line_workloads[line] + component[0]
                    <= self.line_capacities[line]
                ):
                    cost = self.calculate_cost(component, line)
                    if cost < min_cost:
                        min_cost = cost
                        best_line = line
            if best_line != -1:
                self.line_workloads[best_line] += component[0]
                self.total_cost += min_cost
            else:
                self.split_component(component)
        return self.total_cost

    def split_component(self, component):
        weight, complexity, lines = component
        remaining_weight = weight
        for line in sorted(lines):
            if remaining_weight == 0:
                break
            available_capacity = self.line_capacities[line] - self.line_workloads[line]
            if available_capacity > 0:
                assign_weight = min(remaining_weight, available_capacity)
                self.line_workloads[line] += assign_weight
                self.total_cost += self.calculate_cost(
                    (assign_weight, complexity, lines), line
                )
                remaining_weight -= assign_weight


def optimize_assembly_lines(components, line_capacities):
    optimizer = AssemblyLineOptimizer(components, line_capacities)
    return optimizer.distribute_components()


# Example usage
components = [(10, 2, {0}), (5, 1, {0}), (8, 3, {0})]
line_capacities = [100]
print(optimize_assembly_lines(components, line_capacities))  # Output: 0
