"""
인접행렬 방식 그래프

graph: [[0, 1, 1, 0],
        [1, 0, 0, 1],
        [0, 0, 0, 1],
        [1, 0, 1, 0]]

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
        for next_node, edge in enumerate(graph[node]):
            if edge == 1 and not V[next_node]:
                V[next_node] = True
                Q.append(next_node)