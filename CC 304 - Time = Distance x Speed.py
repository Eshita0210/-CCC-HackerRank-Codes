import heapq

def dijkstra(graph, start, end):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    queue = [(0, start)]
    while queue:
        current_distance, current_node = heapq.heappop(queue)
        if current_node == end:
            return current_distance
        if current_distance > distances[current_node]:
            continue
        for neighbour, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbour]:
                distances[neighbour] = distance
                heapq.heappush(queue, (distance, neighbour))
    return -1

n, m, p, q, t = map(int, input().split())

graph = {i: {} for i in range(1, n+1)}
for _ in range(m):
    u, v, w = map(int, input().split())
    if u == v:
        continue
    graph[u][v] = w * t
    graph[v][u] = w * t

result = dijkstra(graph, p, q)
print(result)
