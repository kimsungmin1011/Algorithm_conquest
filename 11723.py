T = int(input())
group = []
for _ in range(T):
    a,b=map(str,input().split())

    if a == 'add':
        group.append(int(b))

    elif a == 'check':
        if int(b) in group:
            print(1)
        else:
            print(0)

    elif a == 'remove':
        if int(b) in group:
            group.remove(int(b))

    elif a == 'toggle':
        if int(b) in group:
            group.remove(int(b))
        else:
            group.append(int(b))

    elif a == 'all':
        group = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    elif a == 'empty':
        group = []