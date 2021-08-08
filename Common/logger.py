import logging
from functools import wraps

# DEBUG: Detailed infomration
# INFO: Confirmation that things are working as expected
# WARNING: An indication that something unexpected happened. The software is still working as expected
# SERIOUS:
# CRITICAL:


class Logger():
    def __init__(self, func):
        logging.basicConfig(filename=f'{func.__name__}', level=logging.INFO)
        self.func = func

    def __call__(self, *args, **kwargs):
        logging.info(f'Ran {self.func.__name__} with {args} and {kwargs}')
        return self.func(*args, **kwargs)


@Logger
def add(x, y):
    return x + y


if __name__ == '__main__':
    x = add(5, 2)
    print(x)
