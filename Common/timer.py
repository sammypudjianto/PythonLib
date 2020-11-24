import time
from functools import wraps


def addtimer(orig_func):

    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = orig_func(*args, **kwargs)
        end = time.time()
        print(f'{orig_func.__name__} run took {(end - start):.3f}s')
        return result
    return wrapper


# # example
# @addtimer
# def add(x, y):
#     time.sleep(1)
#     print(f'add {x} {y} run')
#     return x + y


# if __name__ == '__main__':
#     print(add(5, 2))
#     # print(type(x))
