import sys
import heapq

graph = {
    'A':{'B': 3, 'C': 1, 'D': 2},
    'B':{'A': 4, 'D': 3, 'E': 6},
    'C':{'D': 3, 'E': 2, 'F': 4},
    'D':{'A': 3, 'E': 5},
    'E':{'B': 1, 'C': 2, 'D': 5},
    'F':{'A': 5, 'B': 3}
         }

def dijkstra(start):
    distances = {node: sys.maxsize for node in graph}
    distances[start] = 0
    queue = []
    heapq.heappush(queue, [distances[start], start])

    while queue:
        current_distance, node = heapq.heappop(queue)
        if distances[node] < current_distance:
            continue
        for adjacency_node, distance in graph[node].items():
            weighted_distance = current_distance + distance
            if weighted_distance < distances[adjacency_node]:
                distances[adjacency_node] = weighted_distance
                heapq.heappush(queue, [weighted_distance, adjacency_node])
    return distances