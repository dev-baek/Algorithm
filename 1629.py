def mod(base, exp, mod):
    result = 1
    base = base % mod
    
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        exp = exp >> 1
        base = (base * base) % mod
    
    return result

if __name__ == "__main__":
    A, B, C = map(int, input().split())
    print(mod(A, B, C))