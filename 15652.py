def generate_combinations(n, m):
    def back_tracking(start, list):
        if len(list) == m:
            print(*list)
            return
        for i in range(start, n + 1):
            back_tracking(i, list + [i])
    back_tracking(1, [])


if __name__ == "__main__":
    n, m = map(int, input().split())
    generate_combinations(n, m)

