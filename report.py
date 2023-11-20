from collections import deque

A,B,N,M = map(int,input().split())
visited = [False]*100001
def bfs(n,m):
    count = 0
    queue = deque([(n,count)])
    while queue:
        n,count = queue.popleft()
        if n == m:
            return count
        if 0<=n+1<=100000 and visited[n+1] == False:
            queue.append((n+1,count+1))
        if 0<=n-1<=100000:
            queue.append((n-1,count+1))
        if 0<=n+A<=100000:
            queue.append((n+A,count+1))
        if 0<=n-A<=100000:
            queue.append((n-A,count+1))
        if 0<=n*A<=100000:
            queue.append((n*A,count+1))
        if 0<=n+B<=100000:
            queue.append((n+B,count+1))
        if 0<=n-B<=100000:
            queue.append((n-B,count+1))
        if 0<=n*B<=100000:
            queue.append((n*B,count+1))

result = bfs(N,M)
print(result)