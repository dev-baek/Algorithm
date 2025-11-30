from collections import deque
def circular_deque(n, list):
    dq = deque(range(1, n+1))
    count = 0

    for target in list:
        # 타겟의 현재 위치 찾기
        pos = dq.index(target)
        
        # 왼쪽으로 회전하는 것이 더 효율적인지 확인
        if pos <= len(dq) // 2:
            for _ in range(pos):
                dq.append(dq.popleft())
                count += 1
        else:
            for _ in range(len(dq) - pos):
                dq.appendleft(dq.pop())
                count += 1
                
        dq.popleft()
    
    return count

if __name__ == "__main__":
    n, m = map(int, input().split())
    list = list(map(int, input().split()))[:m]
    print(circular_deque(n, list))