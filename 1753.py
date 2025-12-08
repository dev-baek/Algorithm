import heapq
import sys
input = sys.stdin.readline

def dijkstra(graph, start, v):
    dist = [float('inf')] * (v + 1)
    dist[start] = 0
    pq = [(0, start)]

    while pq:
        d, pos = heapq.heappop(pq)
        if d > dist[pos]:
            continue
        for next_pos, weight in graph[pos]:
            cost = d + weight
            if cost < dist[next_pos]:
                dist[next_pos] = cost
                heapq.heappush(pq, (cost, next_pos))
    return dist

if __name__ == "__main__":
    v, e = map(int, input().split())
    k = int(input())
    graph = [[] for _ in range(v + 1)]
    for _ in range(e):
        u, v_node, w = map(int, input().split())
        graph[u].append((v_node, w))
    
    result = dijkstra(graph, k, v)
    
    for i in range(1, v + 1):
        if result[i] == float('inf'):
            print("INF")
        else:
            print(result[i])