import __init__
import matplotlib.pyplot as plt
import numpy as np
from black_scholes import BlackScholes
from Common.timer import addtimer


@addtimer
def sequential(n):
    """
    Sequential option valuation

    Parameters:
    ===========
    n : int
        number of option valuations / strikes
    """

    strikes = np.linspace(80, 120, n)
    option_values = []
    initial_spot = 100
    ir = 0.05
    vol = 0.2
    time_to_maturity = 1
    num_steps = 52
    num_paths = 20000

    for strike in strikes:
        b = BlackScholes(initial_spot, strike, ir, vol, time_to_maturity)
        option_values.append(b.pv_mc(num_steps, num_paths))

    return strikes, option_values


@addtimer
def parallel_compute(n):
    """
    Parallel option valuation

    Parameters:
    ===========
    n : int
        number of strikes
    """
    from ipyparallel import Client

    c = Client(profile='default')
    view = c.load_balanced_view()

    initial_spot = 100
    ir = 0.05
    vol = 0.2
    time_to_maturity = 1
    num_steps = 52
    num_paths = 20000

    strikes = np.linspace(80, 120, n)
    option_values = []
    for strike in strikes:
        bs = BlackScholes(initial_spot, strike, ir, vol, time_to_maturity)
        pv = view.apply_async(bs.pv_mc(num_steps, num_paths))
        option_values.append(pv)

    return strikes, option_values


def plot(x_axis, y_oordinate):
    plt.figure(figsize=(8, 4))
    # plt.plot(strikes, option_pv, 'b')
    plt.plot(strikes, option_pv, 'r')
    plt.grid(True)
    plt.xlabel('strikes')
    plt.ylabel('pv')
    plt.show()


if __name__ == '__main__':
    strikes, option_pv = sequential(20)
    # plot(strikes, option_pv)

    # input()  # user input to pause
    strikes, option_pv = parallel_compute(20)
    plot(strikes, option_pv)
