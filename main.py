import solver
from utils import configure_logger


if __name__ == '__main__':

    configure_logger('INFO', 'logs.txt')
    # G = solver.random_graph(10)
    G = 'graph.txt'
    solution1 = solver.solve(G, method='christofides')
    solution2 = solver.solve(G, method='greedy')
    solution3 = solver.solve(G, method='bnb', save=True)

    print(solution1)
    print(solution2)
    print(solution3)
