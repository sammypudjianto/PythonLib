"""
Loop through using list comprehension to output
[1 1 1 2 4 8 3 9 27 4 16 64]
"""


def looping_number(n, steps):
    return [i ** step for i in range(1, n+1) for step in range(1, steps+1)]


if __name__ == '__main__':
    x = looping_number(4, 3)
    print(x)
