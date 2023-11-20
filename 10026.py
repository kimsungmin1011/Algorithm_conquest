from collections import deque

N = int(input())
graph = [[] for _ in range(N)]
# 일반 방문 리스트
visit = [[False] * N for _ in range(N)]
# 적록색약용 방문 리스트
visit1 = [[False] * N for _ in range(N)]

for i in range(N):
    line = list(input())
    graph[i] = line

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


# 일반 BFS 함수
def bfs(x, y):
    queue = deque([(x, y)])
    while queue:
        x, y = queue.popleft()
        visit[x][y] = True
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (
                0 <= nx < N
                and 0 <= ny < N
                and visit[nx][ny] == False
                and graph[nx][ny] == graph[x][y]
            ):
                queue.append((nx, ny))
                visit[nx][ny] = True


# 적록색약용 BFS 함수
def bfs1(x, y):
    queue = deque([(x, y)])
    while queue:
        x, y = queue.popleft()
        visit1[x][y] = True
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (
                0 <= nx < N
                and 0 <= ny < N
                and visit1[nx][ny] == False
                and graph[nx][ny] == graph[x][y] == "B"
            ):
                queue.append((nx, ny))
                visit1[nx][ny] = True

            # 빨간색과 초록색 차이 구분 못함
            elif (
                0 <= nx < N
                and 0 <= ny < N
                and visit1[nx][ny] == False
                and (
                    graph[nx][ny] == graph[x][y] == "R"
                    or graph[nx][ny] == graph[x][y] == "G"
                    or (graph[nx][ny] == "R" and graph[x][y] == "G")
                    or (graph[nx][ny] == "G" and graph[x][y] == "R")
                )
            ):
                queue.append((nx, ny))
                visit1[nx][ny] = True


# 일반
count = 0
for i in range(N):
    for i2 in range(N):
        if visit[i][i2] == False:
            bfs(i, i2)
            count += 1

# 적록색약
count1 = 0
for i in range(N):
    for i2 in range(N):
        if visit1[i][i2] == False:
            bfs1(i, i2)
            count1 += 1

print(count, count1)
