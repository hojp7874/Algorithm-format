"""
인접리스트 방식 그래프

graph: [[1, 2],
        [0, 3],
        [3],
        [0, 2]]

start_node = 2
"""

graph = list(list,)
def dfs(start_node: int):
    N = len(graph)
    S = [start_node]
    V = [False] * N
    V[start_node] = True
    while S:
        node = S[-1]
        for next_node in graph[node]:
            if not V[next_node]:
                V[next_node] = True
                S.append(next_node)
                break
        else:
            S.pop()