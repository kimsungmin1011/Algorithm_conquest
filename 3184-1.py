from collections import deque

n, m = map(int, input().split())
graph = []
for i in range(n):
    line = list(input())
    graph.append(line)

def bfs(y, x, graph):
    queue = deque([(y, x)])
    ny = [1, -1, 0, 0]
    nx = [0, 0, 1, -1]
    sheep, fox = 0, 0
    if graph[y][x] == 'o':
        sheep += 1
    if graph[y][x] == 'v':
        fox += 1
    graph[y][x] = '#'
    
    while queue:
        y, x = queue.popleft()
        for i in range(4):
            dy = y + ny[i]
            dx = x + nx[i]
            if 0 <= dy < n and 0 <= dx < m:
                if graph[dy][dx] == '.':
                    queue.append((dy, dx))
                    graph[dy][dx] = '#'
                elif graph[dy][dx] == 'v':
                    fox += 1
                    queue.append((dy, dx))
                    graph[dy][dx] = '#'
                elif graph[dy][dx] == 'o':
                    sheep += 1
                    queue.append((dy, dx))
                    graph[dy][dx] = '#'
                    
    if sheep > fox:
        fox = 0
    else:
        sheep = 0
    return sheep, fox

total_sheep, total_fox = 0, 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 'o' or graph[i][j] == 'v':
            sheep, fox = bfs(i, j, graph)
            total_sheep += sheep
            total_fox += fox

print(total_sheep, total_fox)
