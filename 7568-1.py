n = int(input())

stack = []

for i in range(n):
    a,b=map(int,input().split())
    stack.append((a,b))


for i in range(n):
    rank = 1
    for y in range(n):
        if stack[i][0] < stack[y][0] and stack[i][1] < stack[y][1]:
            rank+=1
    print(rank, end=' ')