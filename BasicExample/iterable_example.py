
class MyRange:
    """
    Example of Iterables mimicking 'Range' function in python.
    For iterables, it needs to have __iter__() which returns iterator.
    Iterator needs to have __iter__ and __next__.
    Example of iterables is list. since list has __iter__ but not __next__.
    when you do iter(list), the iterator object will have the __next__
    """
    def __init__(self, start, end, step=1):
        self.value = start
        self.end = end
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if self.value >= self.end:
            raise StopIteration
        current = self.value
        self.value += self.step
        return current


def my_range_gen(start, end, step=1):
    """
    Example of generator that doing the same thing as MyRange class above
    """
    current = start
    while current < end:
        yield current
        current += step


if __name__ == '__main__':
    nums = MyRange(1, 10)
    for i in nums:
        print(i)

    numgen = my_range_gen(1, 10)
    for i in numgen:
        print(i)
