import unittest
from src.problem1 import optimize_assembly_lines

class TestAssemblyLineOptimizer(unittest.TestCase):
    def test_case_1(self):
        components = [(10, 2, {0}), (5, 1, {0}), (8, 3, {0})]
        line_capacities = [100]
        self.assertEqual(optimize_assembly_lines(components, line_capacities), 0)

    def test_case_2(self):
        components = [(10, 2, {0, 1}), (5, 1, {1}), (8, 3, {0})]
        line_capacities = [20, 20]
        self.assertEqual(optimize_assembly_lines(components, line_capacities), 5)

    def test_case_3(self):
        components = [(15, 4, {0, 1}), (10, 2, {0, 1}), (5, 1, {0, 1})]
        line_capacities = [20, 20]
        self.assertEqual(optimize_assembly_lines(components, line_capacities), 10)

    def test_case_4(self):
        components = [(10, 2, {0, 2}), (5, 1, {1, 3}), (8, 3, {2, 3}), (12, 4, {0, 1})]
        line_capacities = [20, 20, 20, 20]
        self.assertEqual(optimize_assembly_lines(components, line_capacities), 18)

if __name__ == '__main__':
    unittest.main()
