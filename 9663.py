import sys
sys.setrecursionlimit(100000)

def n_queen(n):
    cols = [False] * n
    diag1 = [False] * (2 * n - 1)
    diag2 = [False] * (2 * n - 1)

    def backtrack(row):
        if row == n:
            return 1
        count = 0
        for col in range(n):
            d1 = row - col + n - 1
            d2 = row + col
            if cols[col] or diag1[d1] or diag2[d2]:
                continue
            cols[col] = diag1[d1] = diag2[d2] = True
            count += backtrack(row + 1)
            cols[col] = diag1[d1] = diag2[d2] = False
        return count
    return backtrack(0)

if __name__ == "__main__":
    n = int(input())
    print(n_queen(n))