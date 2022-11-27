import string
from itertools import combinations, permutations

a = list(string.ascii_lowercase)
b = ['1', '2', '3']
c = [1, 1, 1, 2]

z = list(map(lambda x, y: x + y, a*3, b*len(a)))

x = set(permutations(c, 4))

print(x)
