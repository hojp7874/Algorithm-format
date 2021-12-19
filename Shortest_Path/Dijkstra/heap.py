"""
힙을 사용한 알고리즘

인접 행렬 그래프

graph: [[INF,  10,  30,  15, INF, INF],
        [INF, INF, INF, INF,  20, INF],
        [INF, INF, INF, INF, INF,   5],
        [INF, INF,   5, INF, INF,  20],
        [INF, INF, INF, INF, INF,  20],
        [INF, INF, INF,  20, INF, INF]]

start_node = 0
"""

import heapq


INF = float('inf')
def dijkstra(graph, start_node):
    N = len(graph)
    heap = [(0, start_node)] # [(dist, node)]
    dist = [INF] * N
    dist[start_node] = 0
    while heap:
        d, node = heapq.heappop(heap)
        if dist[node] < d: # 출발노드와 도착노드가 같은 간선이 2개 이상일 경우 처리
            continue
        for next_node, dd in enumerate(graph[node]):
            #  d: distance
            # dd: delta distance
            # dt: distance total
            dt = d + dd
            if dt < dist[next_node]:
                dist[next_node] = dt
                heapq.heappush(heap, (dt, next_node))
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