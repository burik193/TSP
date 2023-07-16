import numpy as np
import networkx as nx


def reduce_matrix(M: np.matrix):
    """
    Reduces the input matrix by subtracting row and column minima and adjusting infinite values.

    Args:
        M (numpy.matrix): Input matrix.

    Returns:
        tuple: Reduced matrix and the total cost of reduction.
    """
    x_reduce = M.min(axis=0)
    x_reduce[np.isinf(x_reduce)] = 0
    M -= x_reduce
    y_reduce = M.min(axis=1)
    y_reduce[np.isinf(y_reduce)] = 0
    M -= y_reduce
    reduce_cost = x_reduce.sum() + y_reduce.sum()
    return M, reduce_cost


class BnB:
    """
    Class implementing the Branch and Bound algorithm for the Traveling Salesman Problem (TSP).
    """

    def __init__(self, G: nx.Graph):
        """
        Initializes the bnb class instance.

        Args:
            G: Input graph representing the TSP.
        """
        self.adj = dict(G.adjacency())
        self.N = len(self.adj)

        # final_path[] stores the final solution
        # i.e. the path of the salesman.
        self.final_path = []

        # visited[] keeps track of the already
        # visited nodes in a particular path
        self.visited = []

        # Stores the final minimum weight
        # of shortest tour.
        self.final_res = np.inf

        # make adj matrix
        self.M = np.matrix(np.ones((self.N, self.N)) * np.inf)

        for i, j in self.adj.items():
            for k, v in j.items():
                self.M[int(i), int(k)] = v['weight']

    def TSPrecursive(self, M: np.matrix, curr_bound: float, curr_path: np.array):
        """
        Recursive function to find the shortest path for TSP using Branch and Bound.

        Args:
            M (numpy.matrix): Reduced adjacency matrix.
            curr_bound (float): Current lower bound on the path cost.
            curr_path (numpy.ndarray): Current path being explored.

        Returns:
            None
        """
        feasible_path = curr_path[curr_path >= 0]
        y = feasible_path[-1]

        if feasible_path.shape[0] == self.N:
            if M[y, 0] != np.inf:
                curr_path[-1] = 0
                curr_bound += M[y, 0]
                if curr_bound < self.final_res:
                    self.final_res = curr_bound
                    self.final_path = curr_path
            return

        if feasible_path.shape[0] > 1:
            x = feasible_path[-2]
            M[x, :] = np.inf
            M[:, y] = np.inf

        for p in feasible_path:
            M[y, p] = np.inf
        M, reduced_costs = reduce_matrix(M)
        branch = np.array(M[y, :])[0]
        branch = {k: branch[k] for k in np.where((branch < np.inf) & (branch >= 0))[0]}
        branch = dict(sorted(branch.items(), key=lambda _: _[1]))
        for n, cost in branch.items():
            curr_bound += reduced_costs + cost
            if curr_bound < self.final_res:
                curr_path[feasible_path.shape[0]] = n
                self.TSPrecursive(M, curr_bound, np.copy(curr_path))

    def TSP(self):
        """
        Solves the TSP using Branch and Bound algorithm.

        Returns:
            list: The optimal path for the TSP.
        """
        curr_path = np.array([0] + [-1] * self.N)
        M, curr_bound = reduce_matrix(self.M)

        self.TSPrecursive(M, curr_bound, curr_path)
        return list(self.final_path)
