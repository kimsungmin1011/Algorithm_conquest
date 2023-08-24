s = input()
ans = []
i = 0
while i < len(s):
    if s[i] == '.':
        ans.append('.')
        i += 1
    elif s[i:i+4] == 'XXXX':
        ans.append('AAAA')
        i += 4
    elif s[i:i+2] == 'XX':
        ans.append('BB')
        i += 2
    else:
        print(-1)
        exit(0)

print(''.join(ans))
