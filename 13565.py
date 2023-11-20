from collections import deque

M,N = map(int,input().split())

graph = [list(map(int, input().strip())) for _ in range(M)]
visited = [[False] * N for _ in range(M)]

# 이동할 8 방향 정의 (상, 하, 좌, 우, 대각선 포함)
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    queue = deque([(x,y)])
    visited[x][y] = True
    while queue:
        x,y = queue.popleft()
        if x == M-1:
            return 'YES'

        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if 0 <= nx < M and 0 <= ny < N and not visited[nx][ny] and graph[nx][ny] == 0:
                queue.append((nx, ny))
                visited[nx][ny] = True
    return 'NO'

# 바깥쪽에서 전류가 흐르는 지점을 시작점으로 하여 BFS 수행
for i in range(N):
    if graph[0][i] == 0 and not visited[0][i]:
        if bfs(0, i) == 'YES':
            print("YES")
            exit()

print("NO")