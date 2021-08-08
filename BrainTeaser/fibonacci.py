from functools import lru_cache


"""
Below is classic interview questions.
Fibonaci is one example of dynamic programming problem.
"""


@lru_cache(maxsize=5)  # this will help a lot with performance but you will still hit the stack limit.
def fib_rec(n):
    """
    naive recursion. O (exp n) time complexity ,
    """
    if n <= 2:
        return 1
    return fib_rec(n-1) + fib_rec(n-2)


def fib_rec_memo(n):
    """
    naive recursion with memoization.
    Slightly better than fib_rec as it is reused the prev results.
    However still quite bad.
    """
    memo = {}

    def fib(n):
        if n in memo:
            return memo[n]
        if n <= 2:
            memo[n] = 1
        else:
            memo[n] = fib(n-1) + fib(n-2)
        return memo[n]
    return fib(n)


def fib_it(n):
    """
    Faster and more memory efficient method than recursive method.
    This is called bottom up approach.
    As it is only using 2 variables rather than saving the whole stack as the recursion.
    """
    x = 1
    y = 1
    if n <= 2:
        return 1
    for i in range(3, n+1):
        x, y = y, x + y
    return y


if __name__ == '__main__':
    print(fib_rec(400))
    #print(fib_rec_memo(10))
    #print(fib_it(10000))
