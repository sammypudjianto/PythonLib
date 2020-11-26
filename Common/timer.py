import time
from functools import wraps
from timeit import repeat


def addtimer(orig_func):
    """
    Decorater function to time the execution of given function
    params:
        orig_function: python function
    return:
        the original result from the function
    """
    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = orig_func(*args, **kwargs)
        end = time.time()
        print(f'{orig_func.__name__} run took {(end - start) * 1000:.2f}ms')
        return result
    return wrapper


def perf_comp_data(func_list, arg_list, rep=3, number=1):
    """
    Function to compare the performance of different functions.
    (ref : taken from O'Reilly Python for Finance pg 203-204)
    Parameters
    ==========
    func_list : list
        list with function names as strings
    arg_list : list
        list with data set names as strings
    rep : int
        number of repetitions of the whole comparison
    number: int
        number of executions for every function
    """
    res_list = {}
    for i, func_name in enumerate(func_list):
        arg_param = arg_list[i]
        stmt = f'{func_name} ({arg_param})'
        setup = f'from __main__ import {func_name}, {arg_param}'
        results = repeat(stmt, setup, rep, number)
        res_list[func_name] = sum(results) / rep

    res_sort = sorted(res_list.items(), key=res_list.get)

    for k, v in res_sort:
        rel = v / res_sort[0][1]
        print(f'function {k}, avg time sec: {v:.5f}, relative: {rel:.1f}')
