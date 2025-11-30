def coordinate_compression(arr):
    sorted_unique = sorted(set(arr))
    compress = {value: index for index, value in enumerate(sorted_unique)}
    return [compress[x] for x in arr]

if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    print(*coordinate_compression(arr))