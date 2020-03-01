import matplotlib.pyplot as plt
from config import ITERATIONS


def graph_percentages(vec):
    plt.plot(vec)
    plt.savefig(f'graphs/{str(ITERATIONS)}.png')
