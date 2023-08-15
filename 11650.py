import sys

n = int(sys.stdin.readline())

data = []

for i in range(n):
    a,b=map(int,sys.stdin.readline().split())
    data.append((a,b))

data.sort(key=lambda x:(x[0],x[1]))

for i in data:
    print(i[0],i[1])