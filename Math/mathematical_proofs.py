import numpy as np


def proof_of_pi(no_of_sims):
    """
    Proof pi using random numbers
    Given a circle radius = 1
    calculate how many random points fall between 1 distance from the centre.
    multiply by 4 as we only get quarter of a circle
    """
    sum = 0
    for i in range(no_of_sims):
        x = np.random.random()
        y = np.random.random()
        if ((x ** 2) + (y ** 2)) <= 1:
            sum += 1/no_of_sims
    return sum * 4


def proof_of_euler(big_number):
    """
    proof euler number using exponential growth
    """
    return (1 + 1/big_number) ** big_number


if __name__ == '__main__':
    no_paths = 1000000
    print('numerical pi:', proof_of_pi(no_paths))
    print('real pi:', 22/7)
    print('numerical euler:', proof_of_euler(no_paths))
    print('euler', np.exp(1))
