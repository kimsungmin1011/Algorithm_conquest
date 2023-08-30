n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
for i in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

friend = []
for i in graph[1]:
    friend.append(i)
    for i2 in graph[i]:
        friend.append(i2)

kill = set(friend) # 중복 제거
show = list(kill) #중복 제거 후 다시 list화

if show:
    print(len(show)-1)
else:
    print(0)