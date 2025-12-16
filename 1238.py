import heapq
def find_max_time(n, x, graph):
    dist_form_x = dijkstra(x, graph, n)
    reversed_graph = [[] for _ in range(n + 1)]
    for u in range(1, n + 1):
        for v, t in graph[u]:
            reversed_graph[v].append((u, t))
    
    dist_to_x = dijkstra(x, reversed_graph, n)
    max_time = 0
    for i in range(1, n + 1):
        total_time = dist_to_x[i] + dist_form_x[i]
        if total_time > max_time:
            max_time = total_time
    
    return max_time

def dijkstra(start, graph, n):
    dist = [float('inf')] * (n + 1)
    dist[start] = 0
    pq = [(0, start)]

    while pq:
        d, v = heapq.heappop(pq)
        if d > dist[v]:
            continue
        for neighbor, weight in graph[v]:
            new_dist = d + weight
            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                heapq.heappush(pq, (new_dist, neighbor))
    return dist

if __name__ == "__main__":
    n, m ,x = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v, t = map(int, input().split())
        graph[u].append((v, t))

    print(find_max_time(n, x, graph))
