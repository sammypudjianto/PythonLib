from collections import deque
from string import ascii_lowercase


def reverse_k_chars(queue: list,  k_no_chars: int) -> list:
    """
    This function needs to reverse the first k characters
    """
    if len(queue) < k_no_chars:
        raise ValueError('queue need to have greater or equal to length with:', k_no_chars)
    return list(reversed(queue[:k_no_chars])) + queue[k_no_chars:]


if __name__ == '__main__':
    inp = list(ascii_lowercase)
    print(reverse_k_chars(inp, 7))
