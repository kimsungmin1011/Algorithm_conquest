from collections import deque

m,n,k = map(int,input().split())
paper = [[0]*n for _ in range(m)]

for i in range(k):
    x1,y1,x2,y2 = map(int,input().split())
    for i1 in range(y1,y2):
        for i2 in range(x1,x2):
            if paper[i1][i2] == 0:
                paper[i1][i2] = 1

def bfs(y,x,paper):
    queue = deque([(x,y)])
    dy = [0,0,-1,1]
    dx = [1,-1,0,0]
    area_size = 0

    while queue:
        x,y = queue.popleft()
        area_size+=1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<n and 0<=ny<m and paper[ny][nx] == 0:
                paper[ny][nx] = 1
                queue.append((nx,ny))

    return area_size

area = []
for i in range(m):
    for i2 in range(n):
        if paper[i][i2] == 0:
            paper[i][i2] = 1
            area.append(bfs(i,i2,paper))

area.sort()
print(len(area))
print(' '.join(map(str,area)))
