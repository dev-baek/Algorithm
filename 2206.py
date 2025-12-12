from collections import deque
def min_distance(n, m, arr):
    def bfs():
        visited = [[[False] * 2 for _ in range(m)] for _ in range(n)]
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        queue = deque()
        queue.append((0, 0, 1, 0))
        visited[0][0][0] = True

        while queue:
            y, x, distance, broken = queue.popleft()
            if x == m - 1 and y == n - 1:
                return distance
            for dy, dx in directions:
                ny = y + dy
                nx = x + dx
                if 0 <= ny < n and 0 <= nx < m:
                    if arr[ny][nx] == 0 and not visited[ny][nx][broken]:
                        queue.append((ny, nx, distance + 1, broken))
                        visited[ny][nx][broken] = True
                    elif arr[ny][nx] == 1 and broken == 0 and not visited[ny][nx][1]:
                        queue.append((ny, nx, distance + 1, 1))
                        visited[ny][nx][1] = True
        return -1
    return bfs()

if __name__ == "__main__":
    n, m = map(int, input().split())
    arr = []
    for _ in range(n):
        row = list(map(int, list(input().strip())))
        arr.append(row)
    result = min_distance(n, m, arr)
    print(result)