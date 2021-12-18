"""
2차원 공간에서 공간탐색 (ex 미로찾기)

table: [[1, 1, 0, 0],
        [0, 1, 1, 1],
        [0, 1, 0, 0],
        [0, 1, 1, 1]] (1: 이동 가능, 0: 이동 불가능)

start_point = (0, 0)
"""


table = list(list,)
def dfs(start_i: int, start_j: int):
    N = len(table)
    S = [(start_i, start_j)]
    table[start_i][start_j] = 0
    move = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    while S:
        i, j = S[-1]
        for di, dj in move:
            next_i, next_j = i+di, j+dj
            if 0 <= next_i < N and 0 <= next_j < N and table[next_i][next_j] == 1:
                table[next_i][next_j] = 0
                S.append((next_i, next_j))
        else:
            S.pop()