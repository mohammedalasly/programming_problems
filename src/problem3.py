from itertools import permutations

class CityProfitOptimizer:
    def __init__(self, cities, products, knapsack_capacity):
        self.cities = cities
        self.products = products
        self.knapsack_capacity = knapsack_capacity

    def calculate_profit(self, route, quantities):
        profit = 0
        for city in route:
            for product, quantity in quantities.items():
                if product in self.cities[city]["demands"]:
                    profit += self.products[product]["profit"][city] * quantity
        return profit

    def calculate_travel_cost(self, route, quantities):
        total_weight = sum(
            self.products[product]["weight"] * quantity
            for product, quantity in quantities.items()
        )
        cost = 0
        for i in range(len(route) - 1):
            cost += self.cities[route[i]]["neighbors"][route[i + 1]] * total_weight
        return cost

    def optimize_route(self):
        cities_ids = [city["id"] for city in self.cities]
        best_profit = float("-inf")
        best_route = None
        best_quantities = None

        for perm in permutations(cities_ids[1:]):
            route = [cities_ids[0]] + list(perm) + [cities_ids[0]]
            quantities = self.greedy_quantities()
            profit = self.calculate_profit(
                route, quantities
            ) - self.calculate_travel_cost(route, quantities)
            if profit > best_profit:
                best_profit = profit
                best_route = route
                best_quantities = quantities

        return best_route, best_quantities, best_profit

    def greedy_quantities(self):
        quantities = {product["id"]: 0 for product in self.products}
        total_weight = 0
        for product in sorted(
            self.products,
            key=lambda p: max(p["profit"].values()) / p["weight"],
            reverse=True,
        ):
            max_quantity = min(
                self.knapsack_capacity // product["weight"],
                self.cities[0]["demands"].get(product["id"], 0),
            )
            quantities[product["id"]] = max_quantity
            total_weight += max_quantity * product["weight"]
            if total_weight >= self.knapsack_capacity:
                break
        return quantities


def find_optimal_route(cities, products, knapsack_capacity):
    optimizer = CityProfitOptimizer(cities, products, knapsack_capacity)
    return optimizer.optimize_route()


# Example usage
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
print(
    find_optimal_route(cities, products, knapsack_capacity)
)  # Output: (route, quantities, profit)
