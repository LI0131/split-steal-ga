import matplotlib.pyplot as plt
from config import ITERATIONS


def graph_percentages(vec, gtype='population'):
    plt.plot(vec)
    plt.savefig(f'graphs/{gtype}_{str(ITERATIONS)}.png')
