"""
순열 만들기

nPm (permutation)
"""

def permutation(n: int, m: int, arr: list):
    if len(arr) >= m:
        print(' '.join(map(str, arr)))
        return
    for item in range(1, n+1):
        if item not in arr:
            permutation(n, m, arr + [item])

n, m = map(int, input().split())
permutation(n, m, [])

"""
input

3 1
4 2
4 3
4 4
...
"""