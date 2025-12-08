from collections import deque

def grow_baby_shark(space, n):
    shark_size = 2
    time = 0
    eaten_fish = 0
    start_node = find_baby_shark(space, n)
    space[start_node[0]][start_node[1]] = 0

    while True:
        fish = find_fish(space, n, start_node, shark_size)
        if fish == None:
            break
        else :
            start_node = (fish[0], fish[1])
            time += fish[2]
            space[fish[0]][fish[1]] = 0
            eaten_fish += 1
            if eaten_fish == shark_size:
                shark_size += 1
                eaten_fish = 0
    return time

def find_baby_shark(space, n):
    for i in range(n):
        for j in range(n):
            if space[i][j] == 9:
                return i, j

def find_fish(space, n, shark_pos, shark_size):
    visited = [[False] * n for _ in range(n)]
    visited[shark_pos[0]][shark_pos[1]] = True
    queue = deque([(shark_pos[0], shark_pos[1], 0)])
    fish = []

    while queue:
        x, y, distance = queue.popleft()
        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if space[nx][ny] <= shark_size:
                    visited[nx][ny] = True
                    if space[nx][ny] < shark_size and space[nx][ny] > 0:
                        fish.append((distance + 1, nx, ny))
                    queue.append((nx, ny, distance + 1))
    if fish:
        fish.sort()
        dist, x, y = fish[0]
        return (x, y, dist)
    return None

if __name__ == "__main__":
    n = int(input())
    space = [list(map(int, input().split())) for _ in range(n)]
    print(grow_baby_shark(space, n))