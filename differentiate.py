from sympy import *


def diff(func):
    x = symbols('x')
    f_prime = func.diff(x)
    return f_prime


def y():
    x = symbols('x')
    f = x**3 + 2
    return f


def add(x, y):
    return x + y


xn = 3
x = symbols('x')
y = y()

print('y:', y.evalf(subs={x:xn}))
print('y prime:', diff(y).evalf(subs={x:xn}))
