from collections import deque

N, M = map(int, input().split())
graph = [[] * M for _ in range(N)]
for i in range(N):
    line = list(map(int, input().split()))
    graph[i] = line

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

virus_list = []


def bfs():
    queue = deque()
    for t in range(N):
        for f in range(M):
            if graph[t][f] == 2:
                queue.append((t, f))
    for x1 in range(N):
        for x2 in range(M):
            if graph[x1][x2] == 0:
                graph[x1][x2] = 1
    for x3 in range(N):
        for x4 in range(M):
            if graph[x3][x4] == 0:
                graph[x3][x4] = 1
    for x5 in range(N):
        for x6 in range(M):
            if graph[x5][x6] == 0:
                graph[x5][x6] = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 0:
                queue.append((nx, ny))
                graph[nx][ny] = 2
        count = 0
        for x10 in range(N):
            for x11 in range(M):
                if graph[x10][x11] == 0:
                    count += 1
        virus_list.append(count)


bfs()
print(virus_list)
