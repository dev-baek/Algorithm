def pactorial(n):
    if n == 0:
        return 1
    else:
        return n * pactorial(n - 1)
if __name__ == "__main__":
    n = int(input())
    print(pactorial(n))