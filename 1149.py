def color_house(costs, n):
    dp = [[0] * 3 for _ in range(n)]
    dp[0] = costs[0]
    for i in range(1, n):
        dp[i][0] = costs[i][0] + min(dp[i-1][1], dp[i-1][2])
        dp[i][1] = costs[i][1] + min(dp[i-1][0], dp[i-1][2])
        dp[i][2] = costs[i][2] + min(dp[i-1][0], dp[i-1][1])
        
    return min(dp[n-1][0], dp[n-1][1], dp[n-1][2])

if __name__ == "__main__":
    n = int(input())
    costs = []
    for _ in range(n):
        costs.append(list(map(int, input().split())))
    
    print(color_house(costs, n))