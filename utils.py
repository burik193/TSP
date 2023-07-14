import numpy as np
import logging


def configure_logger(level='INFO', logfile=None):
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
    print()


def log(message, level='INFO'):

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
    s = 0
    for c in range(len(l)):
        if c+1 > len(l)-1:
            break
        s += G.get_edge_data(l[c], l[c+1])['weight']
        # print(c)
    return s


def no_duplicates(l: list):
    return len(l[:-1]) == len(set(l))


def dist(p1, p2):
    return np.linalg.norm(p1 - p2)