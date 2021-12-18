"""
인접행렬 방식 그래프

Stack 사용


graph: [[0, 1, 1, 0],
        [1, 0, 0, 1],
        [0, 0, 0, 1],
        [1, 0, 1, 0]]

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
        for next_node, edge in enumerate(graph[node]):
            if edge and not V[next_node]:
                V[next_node] = True
                S.append(next_node)
                break
        else:
            S.pop()