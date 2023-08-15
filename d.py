import sys
sys.setrecursionlimit(10**7)  # 파이썬의 재귀 깊이 한계를 높여줍니다. 너무 깊은 재귀는 프로그램이 종료되는 원인이 될 수 있습니다.

# 이동할 4 방향 정의 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x,y):  # 깊이 우선 탐색(DFS, Depth-First Search) 함수
    visited[x][y]=True  # 현재 위치를 방문했다고 표시
    for i in range(4):  # 4방향에 대해 반복문 수행
        nx = x + dx[i]  # 새로운 x 좌표를 계산
        ny = y + dy[i]  # 새로운 y 좌표를 계산
        # 새로운 위치가 캠퍼스 내부에 있고, 벽(X)이 아니며, 아직 방문하지 않은 경우에만 재귀적으로 DFS 수행
        if (0<=nx<h) and (0<=ny<w) and (map_data[nx][ny] != 'X' ) and not visited[nx][ny]:
            dfs(nx,ny)

h,w=map(int,input().split())  # 캠퍼스의 행(h)과 열(w)의 크기를 입력 받습니다.

# h행 w열의 2차원 리스트 생성. 모든 요소를 False로 초기화하여 아직 방문하지 않은 상태를 표시합니다.
visited = [[False]*w for _ in range(h)]  

# 캠퍼스 맵 데이터 입력. 각 문자를 리스트로 변환하여 2차원 리스트를 생성합니다.
map_data = [list(input()) for _ in range(h)]

people = 0  # 도연이가 만날 수 있는 사람의 수를 저장할 변수

# 모든 위치를 순회하며 'I'가 있는 위치에서 DFS 수행
for i in range(h):
    for j in range(w):
        if map_data[i][j] == 'I' and not visited[i][j]:
            dfs(i, j)

# 다시 모든 위치를 순회하며 'P'가 있는 위치가 방문된 경우에만 사람 수를 카운트
for i in range(h):
    for j in range(w):
        if map_data[i][j] == 'P' and visited[i][j]:
            people += 1

# 만난 사람의 수가 0이 아니면 그 수를 출력하고, 0이면 "TT"를 출력
print(people if people != 0 else "TT")
