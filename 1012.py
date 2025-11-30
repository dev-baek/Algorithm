import sys
sys.setrecursionlimit(10000)

def find_sortest_caterpillar_num(field, m, n):
    def dfs(x, y):
        if x < 0 or x >= m or y < 0 or y >= n or field[x][y] == 0:
            return
        field[x][y] = 0
        
        dfs(x-1 ,y)
        dfs(x ,y-1)
        dfs(x+1 ,y)
        dfs(x ,y+1)
    
    count = 0
    for x in range(m):
        for y in range(n):
            if field[x][y] == 1:
                dfs(x,y)
                count += 1
    return count

if __name__ == "__main__":
    t = int(input())
    results = []
    
    for _ in range(t):
        m, n, k = map(int, input().split())
        field = [[0] * n for _ in range(m)]
        
        for _ in range(k):
            x, y = map(int, input().split())
            field[x][y] = 1
        
        result = find_sortest_caterpillar_num(field, m, n)
        results.append(result)
    
    for result in results:
        print(result) 