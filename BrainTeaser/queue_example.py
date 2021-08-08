"""
This module shows the different way of queue(FIFO) implementation
in python.
lsit is O(n) time and space complexity
queue -> is O(1) , time and space complexity
"""


def queue_list_implementation():
    """
    this is standard queue example in
    """
    queue = []
    queue.append('a')
    queue.append('b')
    queue.append('c')

    print('Initial queue')
    print(queue)

    # Removing elements from the queue
    print('\n Elements dequeued from the queue')
    print(queue.pop(0))
    print(queue.pop(0))
    print(queue.pop(0))

    print('\nQueue after removing elements')
    print(queue)


def queue_deque_implementation():
    from collections import deque
    q = deque()

    for x in 'abc':
        q.append(x)

    print('\nElements dequeued from the queue')
    for _ in range(len(q)):
        print(q.popleft())

    print('\nQueue after removing elements')
    print(q)


if __name__ == '__main__':
    queue_list_implementation()
    queue_deque_implementation()
