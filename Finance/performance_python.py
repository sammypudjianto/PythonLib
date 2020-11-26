import math

import __init__
import numexpr as ne
import numpy as np
from Common.timer import addtimer


class PerformancePython():
    """
    performance comparison between math vs np vs numexpr
    """

    def __init__(self):
        self.num_paths = 500000
        self.a_py = range(self.num_paths)
        self.a_np = np.arange(self.num_paths)

    def f(self, x):
        return abs(math.cos(x)) ** 0.5 + math.sin(2 + 3 * x)

    @addtimer
    def f1(self, a):
        res = []
        for x in a:
            res.append(self.f(x))
        return res

    @addtimer
    def f2(self, a):
        return [self.f(x) for x in a]

    @addtimer
    def f3(self, a):
        ex = 'abs(math.cos(x)) ** 0.5 + math.sin(2 + 3 * x)'
        return [eval(ex) for x in a]

    @addtimer
    def f4(self, a):
        return (np.abs(np.cos(a)) ** 0.5 + np.sin(2 + 3 * a))

    @addtimer
    def f5(self, a):
        ex = 'abs(cos(a)) ** 0.5 + sin(2 + 3 * a)'
        ne.set_num_threads(1)
        return ne.evaluate(ex)

    @addtimer
    def f6(self, a):
        ex = 'abs(cos(a)) ** 0.5 + sin(2 + 3 * a)'
        ne.set_num_threads(16)
        return ne.evaluate(ex)

    def run(self):
        self.f1(self.a_py)
        self.f2(self.a_py)
        self.f3(self.a_py)
        self.f4(self.a_np)
        self.f5(self.a_np)
        self.f6(self.a_np)


if __name__ == '__main__':
    pcompare = PerformancePython()
    pcompare.run()
