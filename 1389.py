from collections import deque

def kebin_rool(graph, n):
    def bfs(start):
        visited = [-1] * (n + 1)
        visited[start] = 0
        queue = deque([start])
        count = 0

        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                if visited[neighbor] == -1 :
                    visited[neighbor] = visited[node] + 1
                    queue.append(neighbor)
        for value in visited:
            if value > 0:
                count += value
        return count
    
    min_count = float('inf')
    for i in range(1, n + 1):
        bfs_result = bfs(i)
        if bfs_result < min_count:
            min_count = bfs_result
            min_user = i

    return min_user

if __name__ == "__main__":
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    print(kebin_rool(graph, n))