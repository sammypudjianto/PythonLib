a = '111591'
b = '13579'


def lcs(s1, n1, s2, n2) -> int:
    if n1 == 0 or n2 == 0:
        return 0

    if s1[n1-1] == s2[n2-1]:
        return 1 + lcs(s1, n1-1, s2, n2-1)

    return max(lcs(s1, n1-1, s2, n2), lcs(s1, n1, s2, n2-1))


x = lcs(a, len(a), b, len(b))
print(x)
