def make_lan_cable(lan_cable, n):
    min_lan = 1
    max_lan = max(lan_cable)
    answer = 0

    while min_lan <= max_lan:
        mid = (min_lan + max_lan) // 2
        num = make_lan_by_size(lan_cable, mid)
        if (num >= n):
            answer = mid
            min_lan = mid + 1
        else:
            max_lan = mid - 1
    return answer

def make_lan_by_size(lan_cable, size):
    num = 0
    for cable in lan_cable:
        num  += cable // size
    return num
if __name__ == "__main__":
    k, n = map(int, input().split())
    lan_cable = [int(input()) for _ in range(k)]
    result = make_lan_cable(lan_cable, n)
    print(result)