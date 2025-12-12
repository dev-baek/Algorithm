if __name__ == "__main__":
    problem = input()
    stack = []
    priority = {'+': 1, '-': 1, '*': 2, '/': 2}
    
    for char in problem:
        if 'A' <= char <= 'Z':
            print(char, end='')
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                print(stack.pop(), end='')
            stack.pop()
        else:
            while stack and stack[-1] != '(' and priority.get(stack[-1], 0) >= priority[char]:
                print(stack.pop(), end='')
            stack.append(char)
    while stack:
        print(stack.pop(), end='')
