"""
조합

nCm (Combination)
"""


def combination(n: int, m: int, arr: list):
    if len(arr) == m+1:
        print(' '.join(map(str, arr[1:])))
        return
    for item in range(arr[-1]+1, n+1):
        combination(n, m, arr + [item])

n, m = map(int, input().split())
combination(n, m, [0])

"""
input

3 1
4 2
4 3
4 4
...
"""