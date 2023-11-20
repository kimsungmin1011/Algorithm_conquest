from collections import deque

# 입력 받기
M, N = map(int, input().split())
banner = [list(map(int, input().split())) for _ in range(M)]

# 방문 여부를 저장하는 배열 초기화
visited = [[False] * N for _ in range(M)]

# 상, 하, 좌, 우, 대각선 방향
directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

def bfs(x, y):
    # 큐에 시작점을 추가하고 방문 표시
    queue = deque([(x, y)])
    visited[x][y] = True
    
    while queue:
        x, y = queue.popleft()
        
        # 상, 하, 좌, 우, 대각선 방향 탐색
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            
            # 범위를 벗어나거나 이미 방문했거나 글자가 아닌 경우 건너뛰기
            if nx < 0 or nx >= M or ny < 0 or ny >= N:
                continue
            if visited[nx][ny] or banner[nx][ny] == 0:
                continue
                
            # 큐에 추가하고 방문 표시
            queue.append((nx, ny))
            visited[nx][ny] = True

# 글자 개수 초기화
count = 0

# 격자를 돌면서 글자 탐색
for i in range(M):
    for j in range(N):
        if banner[i][j] == 1 and not visited[i][j]:
            bfs(i, j)
            count += 1

# 결과 출력
print(count)
