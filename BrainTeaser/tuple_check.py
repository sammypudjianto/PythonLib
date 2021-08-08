import collections

x = ([1, 2, 3], 'str', 5)
j = x[0]
j[0] = 2
print(j)
print(x)

print(f'is variable {x} is hashable? {isinstance(x, collections.Hashable)}')
