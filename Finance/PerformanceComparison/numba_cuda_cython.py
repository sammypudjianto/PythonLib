"""
Speed comparison between straigt python loop vs numba
"""
import time

import matplotlib.pyplot as plt
import numba
import numpy as np


def f_py(i):
    res = 0
    for x in range(i):
        for y in range(i):
            res += 1
    return res


if __name__ == '__main__':

    iterations = np.linspace(1000, 10000, 10, dtype=np.int64)

    res = []
    for iteration in iterations:
        start = time.perf_counter()
        f_py(iteration)
        end = time.perf_counter()
        py_time = (end-start) * 1000

        del_f_py = numba.jit(f_py)
        start = time.perf_counter()
        del_f_py(iteration)
        end = time.perf_counter()
        nb_time = (end-start) * 1000
        res.append((iteration, py_time, nb_time))

    print(' all list', res)
    x = [x for x, y, z in res]
    y = [y for x, y, z in res]
    z = [z for x, y, z in res]
    plt.figure(figsize=(10, 5))
    plt.plot(x, y, 'r')
    plt.plot(x, z, 'b')
    plt.grid(True)
    plt.xlabel('iterations')
    plt.ylabel('time (ms)')
    plt.show()
