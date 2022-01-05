"""
플로이드 워셜
"""

from copy import copy


INF = float("inf")
def floyd_warchall(graph: list):
    N = len(graph)
    dist = copy(graph)
    for node in range(N):
        for waypoint in range(N):
            for next_node in range(N):
                dist_waypoint = dist[node][waypoint] + dist[waypoint][next_node]
                if dist_waypoint < dist[node][next_node]:
                    dist[node][next_node] = dist_waypoint
    return dist


graph = [[INF,  10,  30,  15, INF, INF],
         [INF, INF, INF, INF,  20, INF],
         [INF, INF, INF, INF, INF,   5],
         [INF, INF,   5, INF, INF,  20],
         [INF, INF, INF, INF, INF,  20],
         [INF, INF, INF,  20, INF, INF]]

print(floyd_warchall(graph))