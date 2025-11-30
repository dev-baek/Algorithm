def find_max_value(n, k, item):
    dp = [0] * (k + 1)

    for w, v in item:
        for i in range(k, w - 1, -1):
            dp[i] = max(dp[i], dp[i - w] + v)
    
    return dp[k]

if __name__ == "__main__":
    n, k = map(int, input().split())
    item = [list(map(int, input().split())) for _ in range(n)]
    print(find_max_value(n, k, item))
