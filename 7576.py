from collections import deque

# 입력 받기
M, N = map(int, input().split())
# 빈 리스트의 리스트 생성
box = [list(map(int, input().split())) for _ in range(N)]

# 방향 정의 (위, 아래, 왼쪽, 오른쪽, 앞, 뒤)
dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]


def bfs():
    queue = deque()
    for j in range(N):
        for k in range(M):
            if box[j][k] == 1:
                queue.append((j, k, 0))  # 익은 토마토의 위치와 날짜를 큐에 추가

    while queue:
        y, x, days = queue.popleft()

        for i in range(6):
            ny, nx = y + dy[i], x + dx[i]

            if 0 <= ny < N and 0 <= nx < M and box[ny][nx] == 0:
                box[ny][nx] = 1  # 익은 토마토로 변경
                queue.append((ny, nx, days + 1))

    for j in range(N):
        for k in range(M):
            if box[j][k] == 0:
                return -1  # 모든 토마토가 익지 못한 경우

    return days


result = bfs()
print(result)
