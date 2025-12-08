if __name__ == "__main__":
    string = input()
    bomb = input()
    stack = []

    for char in string:
        stack.append(char)
        if len(stack) >= len(bomb) and ''.join(stack[-len(bomb):]) == bomb:
            del stack[-len(bomb):]

    print(''.join(stack) if stack else 'FRULA')
