import pyximport

pyximport.install()


def f_cy(int x, int y):
    cdef double res = 0
    for i in range(x):
        for j in range(y):
            res += 1
    return res


I, J = 500, 500
f_cy(I, J)
