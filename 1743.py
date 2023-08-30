from collections import deque

n, m, t = map(int, input().split())
graph = [[0] * m for _ in range(n)]
for i in range(t):
    y1, x1 = map(int, input().split())
    graph[y1 - 1][x1 - 1] = 1

def bfs(y, x, graph):
    dy = [1, -1, 0, 0]
    dx = [0, 0, -1, 1]
    size = 1
    queue = deque([(y, x)])
    graph[y][x] = 0  # 방문 처리

    while queue:
        y, x = queue.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < n and 0 <= nx < m and graph[ny][nx] == 1:
                graph[ny][nx] = 0  # 방문 처리
                queue.append((ny, nx))
                size += 1
    return size

size_list = []

for i1 in range(n):
    for i2 in range(m):
        if graph[i1][i2] == 1:  # 음식물 쓰레기 위치 체크
            size_list.append(bfs(i1, i2, graph))

print(max(size_list))
