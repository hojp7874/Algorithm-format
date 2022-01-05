"""
힙을 사용하지 않은 알고리즘

인접 행렬 그래프

graph: [[INF,  10,  30,  15, INF, INF],
        [INF, INF, INF, INF,  20, INF],
        [INF, INF, INF, INF, INF,   5],
        [INF, INF,   5, INF, INF,  20],
        [INF, INF, INF, INF, INF,  20],
        [INF, INF, INF,  20, INF, INF]]

start_node = 0
"""

INF = float('inf')
def dijkstra(graph: list, start_node: int):
    N = len(graph)
    dist = [INF] * N
    dist[start_node] = 0
    V = [False] * N
    d = 0
    node = start_node
    while d < INF:
        min_d = INF
        V[node] = True
        for next_node, dd in enumerate(graph[node]):
            #  d: distance
            # dd: delta distance
            # dt: distance total
            dt = d + dd
            if dt < dist[next_node]:
                dist[next_node] = dt
            if dist[next_node] < min_d and not V[next_node]:
                min_d = dist[next_node]
                min_node = next_node
        d = min_d
        node = min_node
    return dist

# --------------------------------------------------------
graph = [[INF,  10,  30,  15, INF, INF],
         [INF, INF, INF, INF,  20, INF],
         [INF, INF, INF, INF, INF,   5],
         [INF, INF,   5, INF, INF,  20],
         [INF, INF, INF, INF, INF,  20],
         [INF, INF, INF,  20, INF, INF]]
start_node = 0
print(dijkstra(graph, start_node))