def find_start_location(m, n):
    result = []
    for i in range(m-7):
        for j in range(n-7):
            result.append((i, j))
    return result


def find_sortest_num(m, n, arr):
    location = find_start_location(m, n)
    min_changes = 64
    
    for start_i, start_j in location:
        count_start_b = 0
        count_start_w = 0
        for i in range(8):
            for j in range(8):
                current = arr[start_i + i][start_j + j]

                if(i+j)%2 == 0:
                    if current != 'B': count_start_b += 1
                    if current != 'W': count_start_w += 1
                else :
                    if current != 'W': count_start_b += 1
                    if current != 'B': count_start_w += 1
        
        current_min = min(count_start_b, count_start_w)
        min_changes = min(min_changes, current_min)
    
    return min_changes 

if __name__ == "__main__":
    m, n = map(int, input().split())
    arr = []
    for i in range(m):
        row = input().strip()[:n]
        arr.append(row)
    print(find_sortest_num(m, n, arr))
