from collections import deque

def dfs(graph, start_node):
    visited = [False] * (len(graph) + 1)
    result = []
    stack = [start_node]
    
    while stack:
        node = stack.pop()
        if not visited[node]:
            visited[node] = True
            result.append(node)
            for neighbor in reversed(graph[node]):
                if not visited[neighbor]:
                    stack.append(neighbor)
    
    return result

def bfs(graph, start_node):
    visited = [False] * (len(graph) + 1)
    visited[start_node] = True
    queue = deque([start_node])
    result = [start_node]

    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
                result.append(neighbor)
    return result

if __name__ == "__main__":
    n, m, v = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    
    for i in range(1, n+1):
        graph[i].sort()
    print(*dfs(graph, v))
    print(*bfs(graph, v))