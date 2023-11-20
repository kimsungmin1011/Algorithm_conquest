from collections import deque

N = int(input())
ground = [[] for _ in range(N)]
visit = [[False] * N for _ in range(N)]
for i in range(N):
    line = list(map(int, input().split()))
    ground[i] = line

dx = [1, 0]
dy = [0, 1]


def bfs():
    queue = deque([(0, 0)])
    while queue:
        x, y = queue.popleft()
        visit[x][y] = True
        if x == N - 1 and y == N - 1:
            return "HaruHaru"
        for i in range(2):
            nx = x + dx[i] * ground[x][y]
            ny = y + dy[i] * ground[x][y]

            # 해당 위치가 유효한지 먼저 확인한 후 방문 처리
            if 0 <= nx < N and 0 <= ny < N and visit[nx][ny] == False:
                queue.append((nx, ny))
                visit[nx][ny] = True
    return "Hing"


print(bfs())
