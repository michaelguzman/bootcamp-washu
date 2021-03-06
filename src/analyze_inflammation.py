import os
import numpy as np
from matplotlib import pyplot as plt

def center(data, desired=0.0):
    """Return a new array containing the original data centered around the
       desired value (0 by default).

        Example: center([1, 2, 3], 0) => [-1, 0, 1]"""

    return (data -data.mean()) + desired

def plot_data(filename):
    data = np.loadtxt(fname=filename, delimiter=',')

    plt.figure(figsize=(10.0, 3.0))

    plt.subplot(1, 3, 1)
    plt.ylabel('average')
    plt.plot(data.mean(0))

    plt.subplot(1, 3, 2)
    plt.ylabel('max')
    plt.plot(data.max(0))

    plt.subplot(1, 3, 3)
    plt.ylabel('min')
    plt.plot(data.min(0))

    plt.tight_layout()
    plt.show()


def analyze_all(data_path):
    filenames = glob.glob(pattern)
    for f in filenames:
        print f
        plot_data(f)
