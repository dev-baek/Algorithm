def count_pattern(n, m, s):
    count = 0
    i = 0
    
    while i < m - 2:
        if s[i] == "I" and s[i+1] == "O" and s[i+2] == "I":
            temp_count = 1
            i += 3
            
            while i + 1 < m and s[i] == "O" and s[i+1] == "I":
                temp_count += 1
                i += 2
            
            if temp_count >= n:
                count += temp_count - n + 1
        else:
            i += 1
    
    return count

if __name__ == "__main__":
    n = int(input())
    m = int(input())
    s = input()
    print(count_pattern(n, m, s))