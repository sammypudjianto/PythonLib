import unittest


"""
Design an algorithm to find the first unique element in a string.
"""


def get_first_unique_char(word):
    """
    O(n2) time complexity, O(1) for space
    """
    for i, ch in enumerate(word):
        if ch not in word[:i] and ch not in word[i+1:]:
            print(ch)
            return ch

    return -1


def get_first_unique_char_opt(word):
    """
    O(n) time complexity, O(n) for space
    """
    from collections import Counter

    ctr = Counter(word)
    for ch in word:
        if ctr[ch] == 1:
            print(ch)
            return ch
    else:
        return -1


class FirstUniqueCharTest(unittest.TestCase):
    def setUp(self):
        self.func = get_first_unique_char_opt

    def test_unique_char1(self):
        word = 'abcba'  #
        self.assertEqual('c', self.func(word))

    def test_unique_char2(self):
        word = 'bbba'  #
        self.assertEqual('a', self.func(word))

    def test_unique_char3(self):
        word = 'abbb'  #
        self.assertEqual('a', self.func(word))

    def test_unique_char4(self):
        word = 'bbbb'  #
        self.assertEqual(-1, self.func(word))


if __name__ == '__main__':
    unittest.main()
