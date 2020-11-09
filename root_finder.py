import sympy


def bisection(func, min_guess, max_guess, err_tolerance):
    """
    Find the root of a function using bisection method. (Bracketing method)
    arguments:
    func: f(x)
    min_guess: minimum x as guess
    max_guess: maximum x as guess
    err_tolerance: value where f(root) must be less than err_tolerance
    """

    x_new = 0.5 * (min_guess + max_guess)
    y_mid = func(x_new)
    print("x_new: ", x_new)
    if abs(y_mid) < err_tolerance:
        return x_new
    else:
        min_guess = x_new if y_mid <= 0 else min_guess
        max_guess = x_new if y_mid > 0 else max_guess
        return bisection(func, min_guess, max_guess, err_tolerance)


def regula_falsi(func, min_guess, max_guess, err_tolerance):
    """
    Find the root of a function using false position method. (Bracketing method)
    arguments:
    func: f(x)
    min_guess: minimum x as guess
    max_guess: maximum x as guess
    err_tolerance: value where f(root) must be less than err_tolerance
    """
    y_min = func(min_guess)
    y_max = func(max_guess)
    x_new = (y_max - y_min)/(max_guess - min_guess)
    y_new = func(x_new)
    if abs(y_new) <= err_tolerance:
        return x_new
    else:
        min_guess = x_new if y_new <= 0 else min_guess
        max_guess = x_new if y_new > 0 else max_guess
        return regula_falsi(func, min_guess, max_guess, err_tolerance)


def secant(func, min_guess, max_guess, err_tolerance, max_try=10000):
    """
    Find the root of a function using secant method. (Newton method)
    arguments:
    func: f(x)
    min_guess: minimum x as guess
    max_guess: maximum x as guess
    err_tolerance: value where f(root) must be less than err_tolerance
    """
    y_min = func(min_guess)
    y_max = func(max_guess)
    x_new = max_guess - (y_max * (min_guess - max_guess)/(y_min - y_max))
    y_new = func(x_new)
    print("x_new: ", x_new)
    if abs(y_new) <= err_tolerance:
        return x_new
    elif max_try == 0:
        return ValueError('Unable to find root after try')
    else:
        min_guess = x_new if y_new <= 0 else min_guess
        max_guess = x_new if y_new > 0 else max_guess
        return secant(func, min_guess, max_guess, err_tolerance, max_try - 1)


def newton_rhapson(func, min_guess, max_guess, err_tolerance):
    pass


def brent(func, min_guess, max_guess, err_tolerance):
    pass


def j(funct):
    return funct


def f(x):
    return ((x+3) ** 3) - 3


# find root
# root = bisection(f, -5, 5, 0.001)
# print('root for bisection is: ', root)

# root = regula_falsi(f, -5, 5, 0.0001)
# print('root for regula falsi is: ', root)

root = secant(f, -5, -4.9, 0.0001)
print('root for secant is: ', root)

al = j(f)
print(al(root))
