from collections import deque

n,m = map(int,input().split())
graph = []

for i in range(m):
    graph.append(list(input()))

def bfs(x,y,graph):
    queue = deque([(x,y)])
    nx = [1,-1,0,0]
    ny = [0,0,-1,1]
    white = 1
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            dx = x + nx[i]
            dy = y + ny[i]
            if 0<=dx<n and 0<=dy<m and graph[dy][dx] == 'W':
                white+=1
                queue.append((dx,dy))
                graph[dy][dx] = 'C'
    return white**2

def bfs2(x,y,graph):
    queue = deque([(x,y)])
    nx = [1,-1,0,0]
    ny = [0,0,-1,1]
    black = 1
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            dx = x + nx[i]
            dy = y + ny[i]
            if 0<=dx<n and 0<=dy<m and graph[dy][dx] == 'B':
                black+=1
                queue.append((dx,dy))
                graph[dy][dx] = 'C'
    return black**2

white_sum = 0
black_sum = 0
for i in range(m):
    for i1 in range(n):
        if graph[i][i1] == 'W':
            graph[i][i1] = 'C'
            white_sum+=bfs(i1,i,graph)
        elif graph[i][i1] == 'B':
            graph[i][i1] = 'C'
            black_sum+=bfs2(i1,i,graph)

print(white_sum,black_sum)

