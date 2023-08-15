n = int(input())

for _ in range(n):
    a = input()
    stack = []
    for char in a:
        if char == '(':
            stack.append(char)
        else:
            if stack:
                stack.pop()
            else:
                print('NO')
                break
    else:
        if stack:
            print('NO')
        else:
            print('YES')