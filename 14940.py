from collections import deque

def shortest_distance(arr):
    start_node = None
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] == 2:
                start_node = (i, j)
                break
        if start_node:
            break
    
    result = bfs(arr, start_node)

    return result

def bfs(arr, start_node):
    distance = [[-1] * len(arr[0]) for _ in range(len(arr))]
    distance[start_node[0]][start_node[1]] = 0
    
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    queue = deque([start_node])

    while queue:
        y, x = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if ny < 0 or ny >= len(arr) or nx < 0 or nx >= len(arr[0]):
                continue
            if arr[ny][nx] == 1 and distance[ny][nx] == -1:
                distance[ny][nx] = distance[y][x] + 1
                queue.append((ny, nx))
    
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] == 0:
                distance[i][j] = 0
    
    return distance

if __name__ == "__main__":
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    result = shortest_distance(arr)

    for i in range(len(result)):
        print(*(result[i]))
