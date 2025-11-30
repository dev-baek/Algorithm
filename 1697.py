from collections import deque

def find_minimum_time(n, k):
    if n >= k:
        return n - k
    
    dp = [-1] * 100001
    dp[n] = 0
    queue = deque([n])
    
    while queue:
        current = queue.popleft()
        
        if current == k:
            return dp[current]
        
        for next_pos in (current - 1, current + 1, current * 2):
            if 0 <= next_pos < 100001 and dp[next_pos] == -1:
                dp[next_pos] = dp[current] + 1
                queue.append(next_pos)
    
    return dp[k]

if __name__ == "__main__":
    n, k = map(int, input().split())
    print(find_minimum_time(n, k))
