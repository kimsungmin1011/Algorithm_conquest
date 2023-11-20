from collections import deque

n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]

for i in range(m):
    x,y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

def bfs(t,graph):
    queue = deque([(t,0)])
    bacon = 0
    visited = [False] * (n+1)
    while queue:
        t,count = queue.popleft()
        bacon+=count
        for i in graph[t]:
            if not visited[i]:
                visited[i] = True
                queue.append((i,count+1))
    return bacon

total = []
for i in range(1,n+1):
    total.append(bfs(i,graph))

for i in range(len(total)):
    if total[i] == min(total):
        print(i+1)
        break