from collections import deque

def tomato(box, n, m):
    queue = deque()
    
    for i in range(n):
        for j in range(m):
            if box[i][j] == 1:
                queue.append((i, j, 0))
    
    while queue:
        y, x, day = queue.popleft()
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        
        for dy, dx in directions:
            ny = y + dy
            nx = x + dx
            if 0 <= ny < n and 0 <= nx < m:
                if box[ny][nx] == 0:
                    box[ny][nx] = 1
                    queue.append((ny, nx, day + 1))

    for i in range(n):
        for j in range(m):
            if box[i][j] == 0:
                return -1
    
    return day

if __name__ == "__main__":
    m, n = map(int, input().split())
    box = []
    for _ in range(n):
        row = list(map(int, input().split()))[:m]
        box.append(row)
    
    result = tomato(box, n, m)
    print(result)
