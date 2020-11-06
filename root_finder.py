def bisection(func, min_guess, max_guess, err_tolerance):
    """
    Find the root of a function using bisection method.
    arguments:
    func: f(x)
    min_guess: minimum x as guess
    max_guess: maximum x as guess
    err_tolerance: value where f(root) must be less than err_tolerance
    """

    x_new = 0.5 * (min_guess + max_guess)
    y_mid = func(x_new)
    if abs(y_mid) < err_tolerance:
        return x_new
    elif y_mid < 0:
        return bisection(func, x_new, max_guess, err_tolerance)
    else:
        return bisection(func, min_guess, x_new, err_tolerance)


def newton_rhapson(func, min_guess, max_guess, err_tolerance):
    pass


def brent(func, min_guess, max_guess, err_tolerance):
    pass


def j(funct):
    return funct


def f(x):
    return ((x+3) ** 3) - 3


# find root
root = bisection(f, -5, 5, 0.0001)
print('root for x square are: ', root)

al = j(f)
print(al(root))
