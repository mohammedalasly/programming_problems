import unittest
from src.problem2 import allocate_resources


class TestProjectAllocator(unittest.TestCase):
    def test_case_1(self):
        projects = [
            {
                "id": 1,
                "skills": ["A", "B"],
                "budget": 100,
                "dependencies": [],
                "complexity": 1,
            },
            {
                "id": 2,
                "skills": ["C", "D"],
                "budget": 100,
                "dependencies": [],
                "complexity": 1,
            },
        ]
        employees = [
            {"id": 1, "skills": {"A": 0.9, "B": 0.9, "C": 0.1, "D": 0.1}, "cost": 50},
            {"id": 2, "skills": {"A": 0.1, "B": 0.1, "C": 0.9, "D": 0.9}, "cost": 50},
            {"id": 3, "skills": {"A": 0.5, "B": 0.5, "C": 0.5, "D": 0.5}, "cost": 50},
        ]
        expected_output = {1: [1, 3], 2: [2, 3]}
        self.assertEqual(allocate_resources(projects, employees), expected_output)

    def test_case_2(self):
        projects = [
            {
                "id": 1,
                "skills": ["A", "B"],
                "budget": 100,
                "dependencies": [],
                "complexity": 1,
            },
            {
                "id": 2,
                "skills": ["A", "B"],
                "budget": 60,
                "dependencies": [],
                "complexity": 1,
            },
        ]
        employees = [
            {"id": 1, "skills": {"A": 0.9, "B": 0.9}, "cost": 90},
            {"id": 2, "skills": {"A": 0.6, "B": 0.6}, "cost": 60},
            {"id": 3, "skills": {"A": 0.5, "B": 0.5}, "cost": 50},
        ]
        expected_output = {1: [1], 2: [3]}
        self.assertEqual(allocate_resources(projects, employees), expected_output)

    def test_case_3(self):
        projects = [
            {
                "id": 1,
                "skills": ["A"],
                "budget": 100,
                "dependencies": [],
                "complexity": 1,
            },
            {
                "id": 2,
                "skills": ["B"],
                "budget": 100,
                "dependencies": [1],
                "complexity": 1,
            },
            {
                "id": 3,
                "skills": ["C"],
                "budget": 100,
                "dependencies": [2],
                "complexity": 1,
            },
        ]
        employees = [
            {"id": 1, "skills": {"A": 0.9, "B": 0.5, "C": 0.1}, "cost": 50},
            {"id": 2, "skills": {"A": 0.1, "B": 0.9, "C": 0.5}, "cost": 50},
            {"id": 3, "skills": {"A": 0.5, "B": 0.1, "C": 0.9}, "cost": 50},
        ]
        expected_output = {1: [1], 2: [2], 3: [3]}
        self.assertEqual(allocate_resources(projects, employees), expected_output)

    def test_case_4(self):
        projects = [
            {
                "id": 1,
                "skills": ["A", "B"],
                "budget": 150,
                "dependencies": [],
                "complexity": 2,
            },
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
        employees = [
            {"id": 1, "skills": {"A": 0.9, "B": 0.7, "C": 0.3, "D": 0.1}, "cost": 80},
            {"id": 2, "skills": {"A": 0.1, "B": 0.9, "C": 0.7, "D": 0.3}, "cost": 80},
            {"id": 3, "skills": {"A": 0.3, "B": 0.1, "C": 0.9, "D": 0.7}, "cost": 80},
            {"id": 4, "skills": {"A": 0.7, "B": 0.3, "C": 0.1, "D": 0.9}, "cost": 80},
            {"id": 5, "skills": {"A": 0.5, "B": 0.5, "C": 0.5, "D": 0.5}, "cost": 70},
        ]
        expected_output = {1: [1, 5], 2: [2, 5], 3: [3, 5], 4: [4, 5]}
        self.assertEqual(allocate_resources(projects, employees), expected_output)


if __name__ == "__main__":
    unittest.main()
