"""
2차원 공간에서 공간탐색 (ex 미로찾기)

table: [[1, 1, 0, 0],
        [0, 1, 1, 1],
        [0, 1, 0, 0],
        [0, 1, 1, 1]] (1: 이동 가능, 0: 이동 불가능)

start_point = (0, 0)
"""


table = list(list,)
start_i, start_j = int, int
table[start_i][start_j] = 0
move = [(1, 0), (0, 1), (-1, 0), (0, -1)]
def dfs(i: int, j: int):
    N = len(table)
    for di, dj in move:
        next_i, next_j = i+di, j+dj
        if 0 <= next_i < N and 0 <= next_j < N and table[next_i][next_j] == 1:
            table[next_i][next_j] = 0
            dfs(next_i, next_j)