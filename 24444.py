from collections import deque

N,M,R = map(int,input().split())
graph = [[] for _ in range(N)]
visited = [False] * N  # 1차원 불리언 값 목록을 사용합니다

for i in range(N):
    x,y = map(int,input().split())
    graph[x].append(y)
    graph[x].sort()

def bfs(x):
    queue=deque([x])
    visited[x] = True
    while queue:
        s = queue.popleft()
        print(s)
        for i in graph[s]:
            if visited[i] == False:
                queue.append(i)
                visited[i] = True
    print(0)
    
bfs(R)