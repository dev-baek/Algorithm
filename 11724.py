import sys
sys.setrecursionlimit(10000)

def find_connected_component_num(graph, n):
    visited = [False] * (n + 1)
    count = 0
    
    def dfs(node):
        visited[node] = True
        for neighbor in graph[node]:
            if not visited[neighbor]:
                dfs(neighbor)
    
    for i in range(1, n + 1):
        if not visited[i]:
            dfs(i)
            count += 1 
    
    return count
    
if __name__ == "__main__":
    input = sys.stdin.readline
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    result = find_connected_component_num(graph, n)
    print(result)