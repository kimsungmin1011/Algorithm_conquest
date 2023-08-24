from collections import deque

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

# 4방향 (상, 하, 좌, 우) 정의
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    count = 1  # 현재 집 수
    queue = deque([(x, y)])
    graph[x][y] = 0  # 방문 처리

    while queue:
        x, y = queue.popleft()

        # 4방향 탐색
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 지도 범위 내에서
            if 0 <= nx < n and 0 <= ny < n:
                # 집이 있고, 아직 방문하지 않은 경우
                if graph[nx][ny] == 1:
                    queue.append((nx, ny))
                    graph[nx][ny] = 0  # 방문 처리
                    count += 1

    return count

results = []  # 각 단지별 집의 수를 저장하는 리스트

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            results.append(bfs(i, j)) # 1인 부분 (방문처리 되지 않은 부분)에 bfs를 실행하면 해당 단지 내 나머지 1들은 다 방문처리(0) 된다

results.sort()

print(len(results))  # 단지 수 출력
for result in results:
    print(result)  # 각 단지별 집의 수 출력
