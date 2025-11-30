def worm_virus(graph):
    visted = [False] * (len(graph) + 1)
    def dfs(node):
        visted[node] = True
        count = 1
        for i in graph[node]:
            if not visted[i]:
                count += dfs(i)
        return count

    return dfs(1) - 1
        

if __name__ == "__main__":
    n = int(input())
    m = int(input())
    graph = [[] for _ in range(n + 1)]
    
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    print(worm_virus(graph))