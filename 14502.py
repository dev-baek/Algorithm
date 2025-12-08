from collections import deque
from itertools import combinations

def find_safe_space(n, m, space):
    wall_list = wall_combinations(n, m, space)
    virus_list = find_virus(n, m, space)
    max_safe_area = 0

    for i in range(len(wall_list)):
        temp_space = wall_setting(space, wall_list[i])
        for virus in virus_list:
            temp_space = virus_spread(n, m, temp_space, virus)
        safe_area = count_safe_area(n, m, temp_space)
        max_safe_area = max(max_safe_area, safe_area)
    return max_safe_area

def wall_combinations(n, m, space):
    empty_spot = []
    wall_list = []
    for i in range(n):
        for j in range(m):
            if space[i][j] == 0:
                empty_spot.append((i, j))
    wall_list = list(combinations(empty_spot, 3))
    return wall_list

def wall_setting(space, walls):
    temp_space = [row[:] for row in space]
    for wall in walls:
        x, y = wall
        temp_space[x][y] = 1
    return temp_space

def find_virus(n, m, space):
    virus_list = []
    for i in range(n):
        for j in range(m):
            if space[i][j] == 2:
                virus_list.append((i, j))
    return virus_list

def virus_spread(n, m, space, start_node):
    temp_space = [row[:] for row in space]
    visited = [[False] * m for _ in range(n)]
    visited[start_node[0]][start_node[1]] = True
    queue = deque([(start_node[0], start_node[1])])

    while queue:
        x, y = queue.popleft()
        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m:
                if temp_space[nx][ny] == 0 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    temp_space[nx][ny] = 2
                    queue.append((nx, ny))
    return temp_space

def count_safe_area(n, m, space):
    safe_count = 0
    for i in range(n):
        for j in range(m):
            if space[i][j] == 0:
                safe_count += 1
    return safe_count

if __name__ == "__main__":
    n, m = map(int, input().split())
    space = [list(map(int, input().split())) for _ in range(n)]
    print(find_safe_space(n, m, space))