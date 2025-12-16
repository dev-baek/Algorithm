MOD = 1000000007

def fib_pair(n):
    if n == 0:
        return (0, 1)

    a, b = fib_pair(n // 2)

    c = a * (2*b - a) % MOD
    d = (a*a + b*b) % MOD

    if n % 2 == 0:
        return (c, d)
    else:
        return (d, (c + d) % MOD)
    
if __name__ == "__main__":
    n = int(input())
    print(fib_pair(n)[0])