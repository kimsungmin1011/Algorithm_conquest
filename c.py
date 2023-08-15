import sys
sys.setrecursionlimit(10**7)

# 이동할 8 방향 정의 (상, 하, 좌, 우, 대각선 포함)
dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

# 깊이 우선 탐색 함수
def dfs(x, y):
    visited[x][y] = True  # 방문 처리
    for i in range(8):  # 8 방향에 대해서
        nx, ny = x + dx[i], y + dy[i]
        # 범위를 벗어나지 않고, 아직 방문하지 않은 섬인 경우
        if nx >= 0 and nx < h and ny >= 0 and ny < w and map_data[nx][ny] and not visited[nx][ny]:
            dfs(nx, ny)  # 재귀적으로 탐색

while True:
    w, h = map(int, input().split())  # 지도의 가로, 세로 크기 입력 받기
    if w == 0 and h == 0:  # 0, 0이 입력되면 종료
        break

    map_data = [list(map(int, input().split())) for _ in range(h)]  # 지도 데이터 입력 받기
    visited = [[False]*w for _ in range(h)]  # 방문 여부를 기록할 리스트 초기화
    count = 0  # 섬의 개수 초기화

    for i in range(h):
        for j in range(w):
            if map_data[i][j] and not visited[i][j]:  # 아직 방문하지 않은 섬인 경우
                dfs(i, j)  # 해당 섬에서 시작하는 깊이 우선 탐색 수행
                count += 1  # 섬의 개수 1 증가

    print(count)  # 섬의 개수 출력
