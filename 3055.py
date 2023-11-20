from collections import deque

# 입력 받기
R, C = map(int, input().split())
forest = [list(input()) for _ in range(R)]

# 방향 설정 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


# 너비 우선 탐색 함수 정의
def bfs():
    # 고슴도치와 물의 초기 위치를 찾아서 큐에 추가
    water_queue = deque()
    hedgehog_queue = deque()
    for i in range(R):
        for j in range(C):
            if forest[i][j] == "*":
                water_queue.append((i, j))
            elif forest[i][j] == "S":
                hedgehog_queue.append((i, j, 0))
            elif forest[i][j] == "D":
                destination = (i, j)

    while hedgehog_queue:
        # 현재 큐에 있는 물을 먼저 확장
        for _ in range(len(water_queue)):
            x, y = water_queue.popleft()
            for d in range(4):
                nx, ny = x + dx[d], y + dy[d]
                if 0 <= nx < R and 0 <= ny < C and forest[nx][ny] == ".":
                    forest[nx][ny] = "*"
                    water_queue.append((nx, ny))

        # 현재 큐에 있는 고슴도치 위치 이동
        for _ in range(len(hedgehog_queue)):
            x, y, time = hedgehog_queue.popleft()
            for d in range(4):
                nx, ny = x + dx[d], y + dy[d]
                if 0 <= nx < R and 0 <= ny < C:
                    if (nx, ny) == destination:
                        return time + 1
                    elif forest[nx][ny] == ".":
                        forest[nx][ny] = "S"
                        hedgehog_queue.append((nx, ny, time + 1))

    return "KAKTUS"


print(bfs())
