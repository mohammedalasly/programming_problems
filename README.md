# Introduction

This project consists of three Python scripts that solve different optimization problems. The scripts are:

1. `min_cost_distribution.py`
2. `calculate_project_value.py`
3. `calculate_total_profit.py`

Each script is designed to solve specific problems, but some of the solutions provided are not fully successful.

## Scripts and Issues

1. **min_cost_distribution.py**

* This script attempts to distribute components across multiple lines with the goal of minimizing the total cost while adhering to line capacities.

### Issues

**For some inputs, the expected output and the actual output do not match.**

* Test 2: Expected Output: 5, Actual Output: inf
* Test 3: Expected Output: 10, Actual Output: 37
* Test 4: Expected Output: 18, Actual Output: inf

 These discrepancies indicate that the current algorithm does not handle all scenarios correctly, possibly due to incorrect heap operations or logic flaws when selecting the best line for components.

To run the test:

```pash
python min_cost_distribution.py
```

2. **calculate_project_value.py**

* This script is designed to calculate the project value by optimizing the route of products delivered to cities based on demands and profits.

### Issues

**For some test cases, the expected profit and the actual profit do not match.**

* Test 1: Expected Profit: 32, Actual Profit: 0
* Test 2: Expected Profit: 98, Actual Profit: 90
* Test 3: Expected Profit: -3, Actual Profit: 0
* Test 4: Expected Profit: 107, Actual Profit: 57

The discrepancies indicate that the route optimization algorithm might not be correctly maximizing the profit or handling the demands and knapsack capacity constraints properly.

To run the test:

```pash
python calculate_project_value.py
```

3. **calculate_total_profit.py**

This script aims to calculate the total profit based on input parameters like costs and revenues.

### Issues

The output for some inputs does not match the expected results, indicating potential issues in profit calculation or input handling logic.

To run the test:

```pash
python calculate_total_profit.py
```

### Conclusion

The provided scripts implement algorithms for solving complex optimization problems. However, the current implementations have some issues that lead to incorrect outputs in certain test cases. These discrepancies need to be addressed to ensure the algorithms work as intended across all scenarios. Further debugging and testing are required to identify and fix the underlying issues in the logic of each script.
