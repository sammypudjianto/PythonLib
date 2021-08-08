import matplotlib.pyplot as plt
import numpy as np


def quadratic_variation(b):
    return np.cumsum(np.power(np.diff(b, axis=0, prepend=0), 2), axis=0)


if __name__ == '__main__':
    n = 10000
    T = 1
    paths = 5
    t = np.linspace(start=0, stop=T, num=n)
    dt = t[1] - t[0]
    db = np.random.normal(size=(n-1, paths)) * np.sqrt(dt)
    b0 = np.zeros(shape=(1, paths))
    b = np.concatenate((b0, np.cumsum(db, axis=0)), axis=0)
    plt.plot(t, b)
    plt.plot(t, quadratic_variation(b))
    plt.show()
