def climb_stairs (stairs, t):
    if t == 1:
        return stairs[0]
    if t == 2:
        return stairs[0] + stairs[1]
    
    dp = [0] * t
    dp[0] = stairs[0]
    dp[1] = stairs[0] + stairs[1]
    dp[2] = max(stairs[0] + stairs[2], stairs[1] + stairs[2])
    for i in range(3, t):
        dp[i] = max(dp[i-2] + stairs[i], dp[i-3] + stairs[i-1] + stairs[i])
    return dp[t-1]

if __name__ == "__main__" :
    t = int(input())
    stairs = []
    for _ in range(t):
        stairs.append(int(input()))
    result = climb_stairs(stairs, t)
    print(result)