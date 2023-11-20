from collections import deque

R,C = map(int,input().split())
graph = [[]*C for _ in range(R)]
visited = [[False]*C for _ in range(R)]
total = [0,0]

for i in range(R):
    graph[i] = list(input().strip())

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    queue = deque([(x,y)])
    v,k = 0,0
    if graph[x][y] == 'v':
        v+=1
    elif graph[x][y] == 'k':
        k+=1
    while queue:
        x,y = queue.popleft()
        visited[x][y] = True
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<R and 0<=ny<C and visited[nx][ny] == False and graph[nx][ny]!='#':
                queue.append((nx,ny))
                visited[nx][ny] = True
                if graph[nx][ny] == 'v':
                    v+=1
                elif graph[nx][ny] == 'k':
                    k+=1
    if k>v:
        v = 0
        return v,k
    else:
        k = 0
        return v,k

for i in range(R):
    for s in range(C):
        if graph[i][s] != '#' and visited[i][s] == False:
            v, k = bfs(i, s)
            total[0] += k
            total[1] += v

print(total[0],total[1])

