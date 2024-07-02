def calculate_total_profit(route, quantities, cities, products, knapsack_capacity):
    total_profit = 0
    total_weight = sum(products[p]["weight"] * q for p, q in quantities.items())
    if total_weight > knapsack_capacity:
        return -float("inf")  # Invalid solution due to exceeding capacity

    for i in range(len(route) - 1):
        city_id = route[i]
        next_city_id = route[i + 1]
        if next_city_id not in cities[city_id]["neighbors"]:
            return -float("inf")  # Invalid route
        travel_cost = cities[city_id]["neighbors"][next_city_id] * total_weight

        total_profit -= travel_cost
        for product_id, quantity in quantities.items():
            if product_id in cities[city_id]["demands"]:
                total_profit += products[product_id]["profit"][city_id] * min(
                    quantity, cities[city_id]["demands"][product_id]
                )

    return total_profit


def initial_solution(cities, products, knapsack_capacity):
    # Create an initial route visiting all cities and returning to the start
    route = [i for i in range(len(cities))] + [0]

    # Sort products by profit-to-weight ratio
    product_ratios = sorted(
        products, key=lambda p: max(p["profit"].values()) / p["weight"], reverse=True
    )

    # Fill the knapsack greedily
    quantities = {}
    remaining_capacity = knapsack_capacity
    for product in product_ratios:
        product_id = product["id"]
        product_weight = product["weight"]
        max_quantity = remaining_capacity // product_weight
        if max_quantity > 0:
            quantities[product_id] = max_quantity
            remaining_capacity -= max_quantity * product_weight

    return route, quantities


def improve_solution(route, quantities, cities, products, knapsack_capacity):
    best_profit = calculate_total_profit(
        route, quantities, cities, products, knapsack_capacity
    )
    best_route = route[:]
    best_quantities = quantities.copy()

    # Try swapping adjacent cities
    for i in range(1, len(route) - 2):
        new_route = route[:]
        new_route[i], new_route[i + 1] = new_route[i + 1], new_route[i]
        new_profit = calculate_total_profit(
            new_route, best_quantities, cities, products, knapsack_capacity
        )
        if new_profit > best_profit:
            best_profit = new_profit
            best_route = new_route[:]

    # Try adjusting product quantities
    for product_id in quantities:
        new_quantities = quantities.copy()
        if new_quantities[product_id] > 0:
            new_quantities[product_id] -= 1
            new_profit = calculate_total_profit(
                best_route, new_quantities, cities, products, knapsack_capacity
            )
            if new_profit > best_profit:
                best_profit = new_profit
                best_quantities = new_quantities.copy()

        new_quantities = quantities.copy()
        if (
            new_quantities[product_id]
            < knapsack_capacity // products[product_id]["weight"]
        ):
            new_quantities[product_id] += 1
            new_profit = calculate_total_profit(
                best_route, new_quantities, cities, products, knapsack_capacity
            )
            if new_profit > best_profit:
                best_profit = new_profit
                best_quantities = new_quantities.copy()

    return best_route, best_quantities, best_profit


def optimize_route(cities, products, knapsack_capacity):
    # Generate initial solution
    route, quantities = initial_solution(cities, products, knapsack_capacity)

    # Improve the solution iteratively
    while True:
        new_route, new_quantities, new_profit = improve_solution(
            route, quantities, cities, products, knapsack_capacity
        )
        if new_profit <= calculate_total_profit(
            route, quantities, cities, products, knapsack_capacity
        ):
            break
        route, quantities = new_route, new_quantities

    # Calculate final profit
    final_profit = calculate_total_profit(
        route, quantities, cities, products, knapsack_capacity
    )

    return {"route": route, "quantities": quantities, "profit": final_profit}


# Unit Tests
cities1 = [
    {"id": 0, "demands": {0: 10, 1: 5}, "neighbors": {1: 2, 2: 3}},
    {"id": 1, "demands": {0: 7, 1: 8}, "neighbors": {0: 2, 2: 1, 3: 4}},
    {"id": 2, "demands": {0: 3, 1: 6}, "neighbors": {0: 3, 1: 1, 3: 2}},
    {"id": 3, "demands": {0: 4, 1: 9}, "neighbors": {1: 4, 2: 2}},
]
products1 = [
    {"id": 0, "weight": 2, "profit": {0: 5, 1: 3, 2: 1, 3: 2}},
    {"id": 1, "weight": 3, "profit": {0: 2, 1: 4, 2: 3, 3: 5}},
]
knapsack_capacity1 = 5

cities2 = [
    {"id": 0, "demands": {0: 5}, "neighbors": {1: 1}},
    {"id": 1, "demands": {0: 5}, "neighbors": {0: 1}},
]
products2 = [{"id": 0, "weight": 1, "profit": {0: 10, 1: 10}}]
knapsack_capacity2 = 5

cities3 = [
    {"id": 0, "demands": {}, "neighbors": {1: 1, 2: 1}},
    {"id": 1, "demands": {}, "neighbors": {0: 1, 2: 1}},
    {"id": 2, "demands": {}, "neighbors": {0: 1, 1: 1}},
]
products3 = [{"id": 0, "weight": 1, "profit": {0: 0, 1: 0, 2: 0}}]
knapsack_capacity3 = 5

cities4 = [
    {"id": 0, "demands": {0: 1, 1: 1}, "neighbors": {1: 1, 2: 1}},
    {"id": 1, "demands": {0: 1, 1: 1}, "neighbors": {0: 1, 2: 1}},
    {"id": 2, "demands": {0: 1, 1: 1}, "neighbors": {0: 1, 1: 1}},
]
products4 = [
    {"id": 0, "weight": 1, "profit": {0: 10, 1: 20, 2: 30}},
    {"id": 1, "weight": 1, "profit": {0: 30, 1: 20, 2: 10}},
]
knapsack_capacity4 = 2

print(
    optimize_route(cities1, products1, knapsack_capacity1)
)  # Expected Output: {'route': [0, 1, 2, 3, 0], 'quantities': {0: 2, 1: 1}, 'profit': 32} // actuall Output: {'route': [0, 1, 3, 2, 0], 'quantities': {0: 0}, 'profit': 0}
print(
    optimize_route(cities2, products2, knapsack_capacity2)
)  # Expected Output: {'route': [0, 1, 0], 'quantities': {0: 5}, 'profit': 98} // actuall Output: {'route': [0, 1, 0], 'quantities': {0: 5}, 'profit': 90}
print(
    optimize_route(cities3, products3, knapsack_capacity3)
)  # Expected Output: {'route': [0, 1, 2, 0], 'quantities': {0: 0}, 'profit': -3} // actuall Output: {'route': [0, 1, 2, 0], 'quantities': {0: 0}, 'profit': 0}
print(
    optimize_route(cities4, products4, knapsack_capacity4)
)  # Expected Output: {'route': [0, 2, 1, 0], 'quantities': {0: 1, 1: 1}, 'profit': 107} // actuall Output: {'route': [0, 1, 2, 0], 'quantities': {0: 1}, 'profit': 57}
