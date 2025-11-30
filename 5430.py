from collections import deque

def R(reversed_flag):
    return not reversed_flag

def D(arr, reversed_flag):
    if len(arr) <= 0:
        return None
    if reversed_flag == False:
        arr.popleft() 
    else:
        arr.pop()
    return arr

def AC(commands, arr):
    dq = deque(arr)
    reversed_flag = False
    
    for cmd in commands:
        if cmd == 'R':
            reversed_flag = R(reversed_flag)
        elif cmd == 'D':
            result = D(dq, reversed_flag)
            if result is None:
                return "error"
    
    result = list(dq)
    return result[::-1] if reversed_flag else result 

if __name__ == "__main__":
    t = int(input())
    results = []
    for _ in range(t):
        p = input()
        n = int(input())
        arr_input = input()
        arr = eval(arr_input)[:n]
        result = AC(p, arr)
        if result == "error":
            results.append("error")
        else:
            results.append(str(result).replace(' ', ''))
    
    for result in results:
        print(result)
