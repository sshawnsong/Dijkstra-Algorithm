import sys
import heapq
import graph

def getDijkstra(start):
    distances = {node: sys.maxsize for node in graph.nodes}
    distances[start] = 0
    queue = []
    heapq.heappush(queue, [distances[start], start])

    while queue:
        current_distance, node = heapq.heappop(queue)
        if distances[node] < current_distance:
            continue
        for adjacency_node, distance in graph.nodes[node].items():
            weighted_distance = current_distance + distance
            if weighted_distance < distances[adjacency_node]:
                distances[adjacency_node] = weighted_distance
                heapq.heappush(queue, [weighted_distance, adjacency_node])
    return distances