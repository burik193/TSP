import numpy as np
import logging


def configure_logger(level='INFO', logfile=None):
    """
    Configures the logger with the specified log level and log file.

    Args:
        level (str): Log level ('DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL').
        logfile (str): Path to the log file.

    Returns:
        None
    """
    logger = logging.getLogger("console")
    logger.setLevel(level)

    if not logger.handlers:
        if not logfile:
            console_handler = logging.StreamHandler()
            console_handler.setLevel(level)
            logger.addHandler(console_handler)
        else:
            file_handler = logging.FileHandler(logfile)
            file_handler.setLevel(level)
            logger.addHandler(file_handler)


def log(message, level='INFO'):
    """
    Logs a message with the specified log level.

    Args:
        message (str): Message to be logged.
        level (str): Log level ('DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL').

    Returns:
        None
    """
    logger = logging.getLogger("console")

    match level:
        case 'DEBUG':
            logger.debug(message)
        case 'INFO':
            logger.info(message)
        case 'WARNING':
            logger.warning(message)
        case 'ERROR':
            logger.error(message)
        case 'CRITICAL':
            logger.critical(message)
        case _:
            logger.debug(message)


def get_sum(G, l: list):
    """
    Calculates the sum of edge weights in the graph G for the given path.

    Args:
        G: Input graph.
        l (list): Path represented as a list of nodes.

    Returns:
        float: Sum of edge weights for the given path.
    """
    s = 0
    for c in range(len(l)):
        if c+1 > len(l)-1:
            break
        s += G.get_edge_data(l[c], l[c+1])['weight']
    return s


def no_duplicates(l: list):
    """
    Checks if a list contains any duplicate elements.

    Args:
        l (list): Input list.

    Returns:
        bool: True if there are no duplicates, False otherwise.
    """
    return len(l[:-1]) == len(set(l))


def dist(p1, p2):
    """
    Calculates the Euclidean distance between two points.

    Args:
        p1: First point.
        p2: Second point.

    Returns:
        float: Euclidean distance between p1 and p2.
    """
    return np.linalg.norm(p1 - p2)


def random_graph(N: int):
    """
    Generates a random graph with N nodes.

    Args:
        N (int): Number of nodes in the graph.

    Returns:
        nx.Graph: Randomly generated graph.
    """
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