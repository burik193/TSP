# TSP Solver Repository

This repository contains code for solving the Traveling Salesman Problem (TSP) using various algorithms. It provides implementations for graph generation, TSP solving algorithms, logging utilities, and other helper functions.

## Table of Contents

- [Introduction](#introduction)
- [Code](#code)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction

The Traveling Salesman Problem (TSP) is a classic optimization problem in computer science and operations research. Given a list of cities and the distances between them, the goal is to find the shortest possible route that visits each city exactly once and returns to the starting city.

This repository provides different algorithms for solving the TSP, including the Christofides algorithm, greedy algorithm, and Branch and Bound algorithm. It also includes utilities for graph generation, logging, and helper functions.

## Code

The code in this repository is organized into the following files:

- `main.py`: Contains functions for generating random graphs for the TSP problem.
- `solver.py`: Contains implementations of TSP solving algorithms, such as the Christofides algorithm, greedy algorithm, and Branch and Bound algorithm.
- `utils.py`: Contains various utility functions.

## Usage

To use the TSP solver, follow these steps:

1. Install the required dependencies by running `pip install -r requirements.txt`.

2. Test the implementation using `main.py`

   1. Generate a graph using the `random_graph()` function from `utils.py` 
   using <a href='https://networkx.org/documentation/stable/reference/readwrite/generated/networkx.readwrite.edgelist.read_weighted_edgelist.html'>weighted edgelist graph representation</a>.

   2. Choose a TSP solving method (e.g., 'christofides', 'greedy', or 'bnb').

   3. Use the `solve()` function from `solver.py` to solve the TSP and obtain the optimal path and its cost.

   4. Optionally, configure the logger using the `configure_logger()` function from `utils.py` to control the log output.

3. Run your code and observe the results.

For detailed usage instructions, refer to the code examples in the `main.py`.

## Contributing

Contributions to this repository are welcome. If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

When contributing, please follow the existing coding style, add tests if applicable, and ensure that the code is well-documented.

## License

The code is completely open-source. You are free to use, modify, and distribute the code in this repository.

