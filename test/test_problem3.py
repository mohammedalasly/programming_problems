import unittest
from src.problem3 import find_optimal_route


class TestCityProfitOptimizer(unittest.TestCase):
    def test_case_1(self):
        cities = [
            {"id": 0, "demands": {0: 10, 1: 5}, "neighbors": {1: 2, 2: 3}},
            {"id": 1, "demands": {0: 7, 1: 8}, "neighbors": {0: 2, 2: 1, 3: 4}},
            {"id": 2, "demands": {0: 3, 1: 6}, "neighbors": {0: 3, 1: 1, 3: 2}},
            {"id": 3, "demands": {0: 4, 1: 9}, "neighbors": {1: 4, 2: 2}},
        ]
        products = [
            {"id": 0, "weight": 2, "profit": {0: 5, 1: 3, 2: 1, 3: 2}},
            {"id": 1, "weight": 3, "profit": {0: 2, 1: 4, 2: 3, 3: 5}},
        ]
        knapsack_capacity = 5
        expected_output = ([0, 1, 2, 3, 0], {0: 2, 1: 1}, 32)
        self.assertEqual(
            find_optimal_route(cities, products, knapsack_capacity), expected_output
        )

    def test_case_2(self):
        cities = [
            {"id": 0, "demands": {0: 5}, "neighbors": {1: 1}},
            {"id": 1, "demands": {0: 5}, "neighbors": {0: 1}},
        ]
        products = [{"id": 0, "weight": 1, "profit": {0: 10, 1: 10}}]
        knapsack_capacity = 5
        expected_output = ([0, 1, 0], {0: 5}, 98)
        self.assertEqual(
            find_optimal_route(cities, products, knapsack_capacity), expected_output
        )

    def test_case_3(self):
        cities = [
            {"id": 0, "demands": {}, "neighbors": {1: 1, 2: 1}},
            {"id": 1, "demands": {}, "neighbors": {0: 1, 2: 1}},
            {"id": 2, "demands": {}, "neighbors": {0: 1, 1: 1}},
        ]
        products = [{"id": 0, "weight": 1, "profit": {0: 0, 1: 0, 2: 0}}]
        knapsack_capacity = 5
        expected_output = ([0, 1, 2, 0], {0: 0}, -3)
        self.assertEqual(
            find_optimal_route(cities, products, knapsack_capacity), expected_output
        )

    def test_case_4(self):
        cities = [
            {"id": 0, "demands": {0: 1, 1: 1}, "neighbors": {1: 1, 2: 1}},
            {"id": 1, "demands": {0: 1, 1: 1}, "neighbors": {0: 1, 2: 1}},
            {"id": 2, "demands": {0: 1, 1: 1}, "neighbors": {0: 1, 1: 1}},
        ]
        products = [
            {"id": 0, "weight": 1, "profit": {0: 10, 1: 20, 2: 30}},
            {"id": 1, "weight": 1, "profit": {0: 30, 1: 20, 2: 10}},
        ]
        knapsack_capacity = 2
        expected_output = ([0, 2, 1, 0], {0: 1, 1: 1}, 107)
        self.assertEqual(
            find_optimal_route(cities, products, knapsack_capacity), expected_output
        )


if __name__ == "__main__":
    unittest.main()
