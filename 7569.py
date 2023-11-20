from collections import deque

# 입력 받기
M, N, H = map(int, input().split())
# 빈 리스트의 리스트 생성
box = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

# 방향 정의 (위, 아래, 왼쪽, 오른쪽, 앞, 뒤)
dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]


def bfs():
    queue = deque()
    for i in range(H):
        for j in range(N):
            for k in range(M):
                if box[i][j][k] == 1:
                    queue.append((i, j, k, 0))  # 익은 토마토의 위치와 날짜를 큐에 추가

    while queue:
        z, y, x, days = queue.popleft()

        for i in range(6):
            nz, ny, nx = z + dz[i], y + dy[i], x + dx[i]

            if 0 <= nz < H and 0 <= ny < N and 0 <= nx < M and box[nz][ny][nx] == 0:
                box[nz][ny][nx] = 1  # 익은 토마토로 변경
                queue.append((nz, ny, nx, days + 1))

    for i in range(H):
        for j in range(N):
            for k in range(M):
                if box[i][j][k] == 0:
                    return -1  # 모든 토마토가 익지 못한 경우

    return days


result = bfs()
print(result)
