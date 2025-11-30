import sys
input = sys.stdin.readline

def find_less_fare(graph, n):
    inf = float('inf')
    fare = [[inf] * (n + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        fare[i][i] = 0
    for a in range(1, n + 1):
        for b, c in graph[a]:
            fare[a][b] = min(fare[a][b], c)
    for transfer in range(1, n + 1):
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                fare[a][b] = min(fare[a][b], fare[a][transfer] + fare[transfer][b])
    return fare

if __name__ == "__main__":
    n = int(input())
    m = int(input())
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))

    result = find_less_fare(graph, n)
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if result[i][j] == float('inf'):
                print(0, end=" ")
            else:
                print(result[i][j], end=" ")
        print()