import math
import timeit

import numexpr as ne
import numpy as np

loops = 10000


def example1():
    a = range(1, loops)
    f = lambda: [3 * math.log(x) + math.cos(x) ** 2 for x in a]
    print('example with math library')
    print(timeit.timeit(f, number=100))


def example2():
    a = np.arange(1, loops)
    f = lambda: 3 * np.log(a) + np.cos(a) ** 2

    print('example with numpy library')
    print(timeit.timeit(f, number=100))


def example3():

    ne.set_num_threads(1)
    def f():
        a = np.arange(1, loops)
        formula = '3 * log(a) + cos(a) ** 2'
        return ne.evaluate(formula)

    print('example with numexpr library 1 thread')
    print(timeit.timeit(f, number=100))


def example4():

    ne.set_num_threads(4)
    def f():
        a = np.arange(1, loops)
        formula = '3 * log(a) + cos(a) ** 2'
        return ne.evaluate(formula)

    print('example with numexpr library 4 thread')
    print(timeit.timeit(f, number=100))


if __name__ == '__main__':
    example1()
    example2()
    example3()
    example4()
