import sys
input = sys.stdin.readline

def create_prefix_sum(n, array):
    prefix = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            prefix[i][j] = array[i-1][j-1] + prefix[i-1][j] + prefix[i][j-1] - prefix[i-1][j-1]
    return prefix

def get_range_sum(prefix, x1, y1, x2, y2):
    return prefix[x2][y2] - prefix[x1-1][y2] - prefix[x2][y1-1] + prefix[x1-1][y1-1]

if __name__ == "__main__":
    n, m = map(int, input().split())
    array = [list(map(int, input().split())) for _ in range(n)]
    
    prefix = create_prefix_sum(n, array)
    
    for _ in range(m):
        x1, y1, x2, y2 = map(int, input().split())
        print(get_range_sum(prefix, x1, y1, x2, y2))
