import numpy as np
# import bnb
import networkx as nx
from utils import dist, get_sum, log
import olegs_bnb as bnb
import time


def random_graph(N: int):
    log(f"Generation random graph with {N} nodes...")
    if N <= 0:
        log("Graph should have more than 1 node!", 'ERROR')
        raise Exception("Graph should have more than 1 node!")
    G = nx.complete_graph(N)
    pos = nx.spring_layout(G)
    for i in range(N):
        for j in range(N):
            if i != j:
                G.edges[i, j]['weight'] = dist(pos[i], pos[j])
    log("Done.")
    return G


def solve(G: nx.Graph or str, method: str, save=False):
    start = time.time()

    if isinstance(G, str):
        G = nx.read_weighted_edgelist(G, nodetype=int)

    else:
        if save:
            nx.write_weighted_edgelist(G, 'graph.txt')

    log("\n\n=====================================================================")
    log(f"Solving graph using {method} algorithm...")
    if method == 'christofides':
        path = nx.approximation.christofides(G)

    elif method == 'greedy':
        path = nx.approximation.greedy_tsp(G)

    elif method == 'bnb':
        # cost = get_sum(G, nx.approximation.christofides(G))
        BNB = bnb.bnb(G)
        path = BNB.TSP()
    else:
        return [], 0

    cost = get_sum(G, path)
    log(f"Done: {time.time() - start:.4f}")
    log(f"Best path: {path}")
    log(f"Best path cost: {cost}")
    log("=====================================================================\n\n")
    return path, cost
