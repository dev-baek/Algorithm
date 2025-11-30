def find_shortest_sequence (n, l):
    for length in range(l, 101):
            x = (n-length*(length-1)/2)/length
            if x.is_integer() and x>=0:
                sequence = [int(x+i) for i in range(length)]
                return ' '.join(map(str, sequence))
    return -1
if __name__ == '__main__':
    n, l = list(map(int, input().split()))
    print(find_shortest_sequence(n, l))
