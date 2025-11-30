def check_group(word):
    array = set()
    prev = ''
    for char in word:
        if char != prev:
            if char in array:
                return False
            array.add(char)
            prev = char
    return True

N = int(input())
result = 0
for i in range(N):
    word = input()
    if check_group(word):
        result += 1
print(result)
