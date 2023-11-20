from collections import deque

# 입력 받기
n, m = map(int, input().split())
grid = []
for _ in range(n):
    row = list(map(int, input().split()))
    grid.append(row)

# 목표 지점 찾기
goal_x, goal_y = None, None
for i in range(n):
    for j in range(m):
        if grid[i][j] == 2:
            goal_x, goal_y = i, j
            break
    if goal_x is not None:
        break

# 방향 벡터 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 거리를 저장할 2차원 배열 초기화
distance = [[-1] * m for _ in range(n)]  # 일단 모두 -1로 초기 세팅
# 시작점 0으로
distance[goal_x][goal_y] = 0

# 0인 부분은 distance 배열에서도 0으로
for i in range(n):
    for i2 in range(m):
        if grid[i][i2] == 0:
            distance[i][i2] = 0

# BFS를 사용하여 거리 계산
queue = deque([(goal_x, goal_y)])

while queue:
    x, y = queue.popleft()

    for d in range(4):
        nx, ny = x + dx[d], y + dy[d]

        # 범위를 벗어나면 무시
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue

        # 이미 방문한 지점이거나 갈 수 없는 지점인 경우
        if distance[nx][ny] != -1 or distance[nx][ny] == 0:
            continue

        # 거리 갱신
        distance[nx][ny] = distance[x][y] + 1
        queue.append((nx, ny))

# 출력
for i in range(n):
    for j in range(m):
        print(distance[i][j], end=" ")
    print()  # 줄 바뀔 때마다 줄 바꿈
