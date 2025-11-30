def max_meeting(arr):
    count = 1
    n = 0
    while n < len(arr) - 1:
        result = find_quickest_meetings(arr, n)
        if result is None:
            break
        n = result
        count += 1  
    return count

def find_quickest_meetings(arr, n):
    for i in range(n + 1, len(arr)):
        if arr[n][1] <= arr[i][0]:
            return i
    return None

if __name__ == "__main__":
    n = int(input())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().split())))
    
    arr.sort(key=lambda x: (x[1], x[0]))
    print(max_meeting(arr))