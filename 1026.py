def minimum_value(A, B, T):
    A = sorted(A)
    B = sorted(B, reverse=True)
    result = 0
    for i in range(T):
        result += A[i] * B[i]
    return result

T = int(input())
A = list(map(int, input().split()))[:T]
B = list(map(int, input().split()))[:T]
print(minimum_value(A, B, T))
