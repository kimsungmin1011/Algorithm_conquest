import sys
sys.setrecursionlimit(10**7)

# 상하좌우를 검사하기 위한 리스트 (2차원 리스트 할 땐 필수적)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 깊이 우선 탐색 함수
def dfs(x, y):
    graph[x][y] = 0  # 현재 위치를 방문 처리합니다.

    # 현재 위치에서 상하좌우로 인접한 위치를 확인합니다.
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        # 인접한 위치가 배추밭 내부이고, 그 위치에 배추가 있으면 재귀적으로 탐색합니다.
        if (0 <= nx < n) and (0 <= ny < m) and (graph[nx][ny] == 1):
            dfs(nx, ny)

# 테스트 케이스 수를 입력받습니다.
for _ in range(int(input())):
    m, n, k = map(int, input().split())  # 배추밭의 크기와 배추의 수를 입력받습니다.
    
    # 배추밭을 0으로 초기화합니다.
    graph = [[0] * m for _ in range(n)]
    
    for _ in range(k):
        y, x = map(int, input().split())  # 배추의 위치를 입력받습니다. (2차원 리스트에선 세로 행을 가로 열보다 먼저 받기 때문에 순서를 반대로 입력)
        graph[x][y] = 1  # 배추 위치를 표시합니다.

    worm = 0  # 필요한 배추흰지렁이 수를 초기화합니다.
    
    # 배추밭을 순회하면서, 아직 방문하지 않은 배추 위치에서 dfs를 실행합니다.
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                dfs(i, j)  # 배추가 있는 곳에서 dfs를 실행합니다.
                worm += 1  # 새로운 배추 집합을 찾았으므로 배추흰지렁이 수를 증가시킵니다.

    print(worm)  # 필요한 배추흰지렁이 수를 출력합니다.
