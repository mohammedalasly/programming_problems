from collections import defaultdict
import itertools


# Helper function to calculate project value
def calculate_project_value(project, assigned_employees):
    value = 0
    for employee in assigned_employees:
        for skill in project["skills"]:
            if skill in employee["skills"]:
                value += employee["skills"][skill]
    value *= project["complexity"]
    return value


# Helper function to check employee eligibility
def is_employee_eligible(project, employee, current_assignments):
    if employee["id"] in current_assignments:
        return False
    if any(skill not in employee["skills"] for skill in project["skills"]):
        return False
    if employee["cost"] > project["budget"]:
        return False
    return True


# Main allocation algorithm
def allocate_resources(projects, employees):
    # Sort projects by complexity and number of dependencies
    projects.sort(key=lambda p: (-p["complexity"], -len(p["dependencies"])))

    best_assignment = {}
    best_value = 0

    def backtrack(project_index, current_assignments, current_value):
        nonlocal best_assignment, best_value
        if project_index == len(projects):
            if current_value > best_value:
                best_assignment = current_assignments.copy()
                best_value = current_value
            return

        project = projects[project_index]
        eligible_employees = [
            e
            for e in employees
            if is_employee_eligible(project, e, current_assignments)
        ]

        for r in range(1, len(eligible_employees) + 1):
            for combination in itertools.combinations(eligible_employees, r):
                total_cost = sum(e["cost"] for e in combination)
                if total_cost <= project["budget"]:
                    current_value += calculate_project_value(project, combination)
                    for e in combination:
                        current_assignments[e["id"]] = project["id"]
                    backtrack(project_index + 1, current_assignments, current_value)
                    current_value -= calculate_project_value(project, combination)
                    for e in combination:
                        del current_assignments[e["id"]]

    backtrack(0, {}, 0)

    # Transform the best_assignment into the required format
    project_employee_map = defaultdict(list)
    for emp_id, proj_id in best_assignment.items():
        project_employee_map[proj_id].append(emp_id)

    return dict(project_employee_map)


# Unit Tests
projects1 = [
    {"id": 1, "skills": ["A", "B"], "budget": 100, "dependencies": [], "complexity": 1},
    {"id": 2, "skills": ["C", "D"], "budget": 100, "dependencies": [], "complexity": 1},
]
employees1 = [
    {"id": 1, "skills": {"A": 0.9, "B": 0.9, "C": 0.1, "D": 0.1}, "cost": 50},
    {"id": 2, "skills": {"A": 0.1, "B": 0.1, "C": 0.9, "D": 0.9}, "cost": 50},
    {"id": 3, "skills": {"A": 0.5, "B": 0.5, "C": 0.5, "D": 0.5}, "cost": 50},
]

projects2 = [
    {"id": 1, "skills": ["A", "B"], "budget": 100, "dependencies": [], "complexity": 1},
    {"id": 2, "skills": ["A", "B"], "budget": 60, "dependencies": [], "complexity": 1},
]
employees2 = [
    {"id": 1, "skills": {"A": 0.9, "B": 0.9}, "cost": 90},
    {"id": 2, "skills": {"A": 0.6, "B": 0.6}, "cost": 60},
    {"id": 3, "skills": {"A": 0.5, "B": 0.5}, "cost": 50},
]

projects3 = [
    {"id": 1, "skills": ["A"], "budget": 100, "dependencies": [], "complexity": 1},
    {"id": 2, "skills": ["B"], "budget": 100, "dependencies": [1], "complexity": 1},
    {"id": 3, "skills": ["C"], "budget": 100, "dependencies": [2], "complexity": 1},
]
employees3 = [
    {"id": 1, "skills": {"A": 0.9, "B": 0.5, "C": 0.1}, "cost": 50},
    {"id": 2, "skills": {"A": 0.1, "B": 0.9, "C": 0.5}, "cost": 50},
    {"id": 3, "skills": {"A": 0.5, "B": 0.1, "C": 0.9}, "cost": 50},
]

projects4 = [
    {"id": 1, "skills": ["A", "B"], "budget": 150, "dependencies": [], "complexity": 2},
    {
        "id": 2,
        "skills": ["B", "C"],
        "budget": 150,
        "dependencies": [1],
        "complexity": 2,
    },
    {
        "id": 3,
        "skills": ["C", "D"],
        "budget": 150,
        "dependencies": [2],
        "complexity": 2,
    },
    {
        "id": 4,
        "skills": ["D", "A"],
        "budget": 150,
        "dependencies": [3],
        "complexity": 2,
    },
]
employees4 = [
    {"id": 1, "skills": {"A": 0.9, "B": 0.7, "C": 0.3, "D": 0.1}, "cost": 80},
    {"id": 2, "skills": {"A": 0.1, "B": 0.9, "C": 0.7, "D": 0.3}, "cost": 80},
    {"id": 3, "skills": {"A": 0.3, "B": 0.1, "C": 0.9, "D": 0.7}, "cost": 80},
    {"id": 4, "skills": {"A": 0.7, "B": 0.3, "C": 0.1, "D": 0.9}, "cost": 80},
    {"id": 5, "skills": {"A": 0.5, "B": 0.5, "C": 0.5, "D": 0.5}, "cost": 70},
]

print(
    allocate_resources(projects1, employees1)
)  # Expected Output: {1: [3], 2: [3]} // actuall Output: {1: [1], 2: [2, 3]}
print(
    allocate_resources(projects2, employees2)
)  # Expected Output: {1: [2], 2: [3]} // atuall Output: {1: [1], 2: [2]}
print(
    allocate_resources(projects3, employees3)
)  # Expected Output: {1: [1], 2: [2], 3: [3]} // atuall Output: {2: [2], 3: [3], 1: [1]}
print(
    allocate_resources(projects4, employees4)
)  # Expected Output: {1: [1, 5], 2: [2, 5], 3: [3, 5], 4: [4, 5]} // atuall Output: {2: [2], 3: [3], 4: [4], 1: [1, 5]}
