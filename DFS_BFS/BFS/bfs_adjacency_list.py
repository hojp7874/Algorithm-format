"""
인접리스트 방식 그래프

graph: [[1, 2],
        [0, 3],
        [3],
        [0, 2]]

start_node = 2
"""

from collections import deque


graph = list(list,)
def bfs(start_node: int):
    N = len(graph)
    Q = deque([start_node])
    V = [False] * N
    V[start_node] = True
    while Q:
        node = Q.popleft()
        for next_node in graph[node]:
            if next_node == 1 and not V[next_node]:
                V[next_node] = True
                Q.append(next_node)