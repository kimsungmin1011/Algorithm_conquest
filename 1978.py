n = int(input())
a = map(int,input().split())

for i1 in a:
    if i1 == 1:
        n-=1
    for i2 in range(2,i1):
        if i1 % i2 == 0:
            n-=1
            break

print(n)