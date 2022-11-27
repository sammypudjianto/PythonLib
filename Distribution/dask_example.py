from dask import delayed, compute
import time

def function_to_delay(id: float):
    time.sleep(1) # sleep for 1s
    print(f'running function to delay {str(id)}')


if __name__=='__main__':
    delayedprocesses = [delayed(function_to_delay)(i) for i in range(1,10)]
    start = time.perf_counter()
    res = compute(delayedprocesses)
    end = time.perf_counter()
    print(f'time run: {(end - start)} seconds')

