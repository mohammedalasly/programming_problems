class ProjectAllocator:
    def __init__(self, projects, employees):
        self.projects = projects
        self.employees = employees
        self.assignments = {}

    def calculate_project_value(self, project, assigned_employees):
        value = 0
        for employee in assigned_employees:
            for skill in project["skills"]:
                value += employee["skills"].get(skill, 0)
        return value

    def check_employee_eligibility(self, project, employee):
        has_skills = all(skill in employee["skills"] for skill in project["skills"])
        within_budget = employee["cost"] <= project["budget"]
        return has_skills and within_budget

    def allocate(self):
        for project in self.projects:
            eligible_employees = [
                e for e in self.employees if self.check_employee_eligibility(project, e)
            ]
            eligible_employees.sort(
                key=lambda e: sum(
                    e["skills"].get(skill, 0) for skill in project["skills"]
                ),
                reverse=True,
            )
            assigned_employees = []
            budget_left = project["budget"]
            for employee in eligible_employees:
                if budget_left >= employee["cost"]:
                    assigned_employees.append(employee)
                    budget_left -= employee["cost"]
            self.assignments[project["id"]] = [e["id"] for e in assigned_employees]
        return self.assignments


def allocate_resources(projects, employees):
    allocator = ProjectAllocator(projects, employees)
    return allocator.allocate()


# Example usage
projects = [
    {"id": 1, "skills": ["A", "B"], "budget": 100, "dependencies": [], "complexity": 1},
    {"id": 2, "skills": ["C", "D"], "budget": 100, "dependencies": [], "complexity": 1},
]
employees = [
    {"id": 1, "skills": {"A": 0.9, "B": 0.9, "C": 0.1, "D": 0.1}, "cost": 50},
    {"id": 2, "skills": {"A": 0.1, "B": 0.1, "C": 0.9, "D": 0.9}, "cost": 50},
    {"id": 3, "skills": {"A": 0.5, "B": 0.5, "C": 0.5, "D": 0.5}, "cost": 50},
]
print(allocate_resources(projects, employees))  # Output: {1: [1, 3], 2: [2, 3]}
