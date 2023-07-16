#!/usr/bin/env python
import networkx as nx
from utils import dist, get_sum, log
from bnb import BnB
import time


def solve(G: nx.Graph or str, method: str, save_graph=False):
    """
    Solves the TSP problem for the given graph using the specified method.

    Args:
        G (nx.Graph or str): Input graph or path to the graph file.
        method (str): TSP solving method ('christofides', 'greedy', or 'bnb').
        save_graph (bool): Flag indicating whether to save the graph to a file.

    Returns:
        tuple: The best path found and its cost.
    """
    start = time.time()

    if isinstance(G, str):
        G = nx.read_weighted_edgelist(G, nodetype=int)
    else:
        if save_graph:
            nx.write_weighted_edgelist(G, 'graph.txt')

    log("\n\n=====================================================================")
    log(f"Solving graph using {method} algorithm...")

    if method == 'christofides':
        path = nx.approximation.christofides(G)

    elif method == 'greedy':
        path = nx.approximation.greedy_tsp(G)

    elif method == 'bnb':
        BNB = BnB(G)
        path = BNB.TSP()

    else:
        return [], 0

    cost = get_sum(G, path)
    log(f"Done: {time.time() - start:.4f}")
    log(f"Best path: {path}")
    log(f"Best path cost: {cost}")
    log("=====================================================================\n\n")
    return path, cost
