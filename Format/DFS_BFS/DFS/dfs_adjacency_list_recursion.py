"""
인접리스트 방식 그래프

재귀 사용


graph: [[1, 2],
        [0, 3],
        [3],
        [0, 2]]

start_node = 2
"""

graph = list(list,)
V = [False] * len(graph)
def dfs(start_node: int):
    for next_node in graph[start_node]:
        if not V[next_node]:
            V[next_node] = True
            dfs(next_node)