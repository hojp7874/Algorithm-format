"""
인접행렬 방식 그래프

재귀 사용


graph: [[0, 1, 1, 0],
        [1, 0, 0, 1],
        [0, 0, 0, 1],
        [1, 0, 1, 0]]

start_node = 2
"""

graph = list(list,)
V = [False] * len(graph)
def dfs(start_node: int):
    for next_node, edge in enumerate(graph[start_node]):
        if edge and not V[next_node]:
            V[next_node] = True
            dfs(next_node)
