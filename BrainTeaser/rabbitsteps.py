import unittest

import fibonacci


"""
 rabbit wants to climb some stairs and it can do steps of 1 or 2 or max_steps
 How many possible paths are there to follow (
 e.g 1-1-1... or 2-2-2 ... or 2-1-2-1... etc)

 This can be also called stair or step traversal.

 Illustration:
 A. total_steps = 5, max steps = 2 = fibonaci
 #ways=  1,1,2,3,5,8,13
 tsteps= 0,1,2,3,4,5,6

 B. total_steps = 5, max steps = 3
 #ways=  1,1,2,4,7,13,24
 tsteps= 0,1,2,3,4,5,6

"""


def count_ways(totsteps: int, max_steps: int) -> int:
    """
    Naive recursive : O(k^n) , memory: stack O(n)
    """
    if totsteps <= 1:
        return 1

    return sum(count_ways(totsteps - i, max_steps) for i in range(1, min(totsteps, max_steps)+1))


def count_ways_iter(totsteps: int, max_steps: int) -> int:
    """
    Bottom up approach and use memoization
    Use rolling window
    """
    memo = [1]

    for step in range(1, totsteps + 1):
        if len(memo) < max_steps:
            memo.append(sum(memo))
        else:
            s = sum(memo)
            memo.pop(0)
            memo.append(s)

    print(memo)
    return memo[-1]


if __name__ == '__main__':
    many_ways = count_ways(5, 2)
    many_ways2 = count_ways_iter(5, 3)
    print(many_ways, many_ways2)
