# Python3 program to solve
# Traveling Salesman Problem using
# Branch and Bound.
import math
import numpy as np


# Function to copy temporary solution
# to the final solution

class bnb:

    def __init__(self, G):
        self.maxsize = float('inf')
        self.adj = dict(G.adjacency())
        self.N = len(self.adj)

        # final_path[] stores the final solution
        # i.e. the // path of the salesman.
        self.final_path = [None] * (self.N + 1)

        # visited[] keeps track of the already
        # visited nodes in a particular path
        self.visited = [False] * self.N

        # Stores the final minimum weight
        # of shortest tour.
        self.final_res = self.maxsize

        # make adj matrix
        self.M = np.matrix(np.ones((self.N, self.N)) * np.inf)

        for i, j in self.adj.items():
            for k, v in j.items():
                self.M[i, k] = v['weight']

    def copyToFinal(self, curr_path):
        self.final_path[:self.N + 1] = curr_path[:]
        self.final_path[self.N] = curr_path[0]

    # Function to find the minimum edge cost
    # having an end at the vertex i
    def firstMin(self, adj, i):
        min = self.maxsize
        for k in range(self.N):
            if adj[i][k] < min and i != k:
                min = adj[i][k]

        return min

    # function to find the second minimum edge
    # cost having an end at the vertex i
    def secondMin(self, adj, i):
        first, second = self.maxsize, self.maxsize
        for j in range(self.N):
            if i == j:
                continue
            if adj[i][j] <= first:
                second = first
                first = adj[i][j]

            elif (adj[i][j] <= second and
                  adj[i][j] != first):
                second = adj[i][j]

        return second


    # function that takes as arguments:
    # curr_bound -> lower bound of the root node
    # curr_weight-> stores the weight of the path so far
    # level-> current level while moving
    # in the search space tree
    # curr_path[] -> where the solution is being stored
    # which would later be copied to final_path[]
    def TSPRec(self, adj, curr_bound, curr_weight,
               level, curr_path, visited):

        # base case is when we have reached level N
        # which means we have covered all the nodes once
        if level == self.N:

            # check if there is an edge from
            # last vertex in path back to the first vertex
            if adj[curr_path[level - 1]][curr_path[0]] != 0:

                # curr_res has the total weight
                # of the solution we got
                curr_res = curr_weight + adj[curr_path[level - 1]] \
                    [curr_path[0]]
                if curr_res < self.final_res:
                    self.copyToFinal(curr_path)
                    self.final_res = curr_res
            return

        # for any other level iterate for all vertices
        # to build the search space tree recursively
        for i in range(self.N):

            # Consider next vertex if it is not same
            # (diagonal entry in adjacency matrix and
            # not visited already)
            if (adj[curr_path[level - 1]][i] != 0 and
                    visited[i] == False):
                temp = curr_bound
                curr_weight += adj[curr_path[level - 1]][i]

                # different computation of curr_bound
                # for level 2 from the other levels
                if level == 1:
                    curr_bound -= ((self.firstMin(adj, curr_path[level - 1]) +
                                    self.firstMin(adj, i)) / 2)
                else:
                    curr_bound -= ((self.secondMin(adj, curr_path[level - 1]) +
                                    self.firstMin(adj, i)) / 2)

                # curr_bound + curr_weight is the actual lower bound
                # for the node that we have arrived on.
                # If current lower bound < final_res,
                # we need to explore the node further
                if curr_bound + curr_weight < self.final_res:
                    curr_path[level] = i
                    visited[i] = True

                    # call TSPRec for the next level
                    self.TSPRec(adj, curr_bound, curr_weight,
                           level + 1, curr_path, visited)

                # Else we have to prune the node by resetting
                # all changes to curr_weight and curr_bound
                curr_weight -= adj[curr_path[level - 1]][i]
                curr_bound = temp

                # Also reset the visited array
                visited = [False] * len(visited)
                for j in range(level):
                    if curr_path[j] != -1:
                        visited[curr_path[j]] = True

    # This function sets up final_path
    def TSP(self):
        # Calculate initial lower bound for the root node
        # using the formula 1/2 * (sum of first min +
        # second min) for all edges. Also initialize the
        # curr_path and visited array
        curr_bound = 0
        curr_path = [-1] * (self.N + 1)
        visited = [False] * self.N
        adj = self.M.tolist()

        # Compute initial bound
        for i in range(self.N):
            curr_bound += (self.firstMin(adj, i) +
                           self.secondMin(adj, i))

        # Rounding off the lower bound to an integer
        curr_bound = math.ceil(curr_bound / 2)

        # We start at vertex 1 so the first vertex
        # in curr_path[] is 0
        visited[0] = True
        curr_path[0] = 0

        # Call to TSPRec for curr_weight
        # equal to 0 and level 1
        self.TSPRec(adj, curr_bound, 0, 1, curr_path, visited)

        return self.final_path
