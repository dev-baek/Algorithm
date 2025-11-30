import heapq
import sys

input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    heap = []
    result = []
    for _ in range(n):
        x = int(input())
        if x == 0:
            if heap:
                result.append(heapq.heappop(heap)[1])
            else:
                result.append(0)
        else:
            heapq.heappush(heap, (abs(x), x))
    for value in result:
        print(value)