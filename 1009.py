def distributed_processing(a, b):
    result = pow(a, b, 10)
    if result == 0:
        result = 10
    return result

T = int(input())
for _ in range(T):
    a, b = map(int, input().split())
    result = distributed_processing(a, b)
    print(result)

