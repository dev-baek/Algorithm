def find_unknown(unknown_hear_name, unknown_see_name):
    result = sorted(list(set(unknown_hear_name) & set(unknown_see_name)))

    return len(result), result

if __name__ == "__main__":
    n, m = map(int, input().split())
    unknown_hear_name = []
    unknown_see_name = []
    for _ in range(n):
        unknown_hear_name.append(input())
    for _ in range(m):
        unknown_see_name.append(input())
    
    count, names = find_unknown(unknown_hear_name, unknown_see_name)
    print(count)
    for name in names:
        print(name)