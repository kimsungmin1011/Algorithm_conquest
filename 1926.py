from collections import deque

m,n = map(int,input().split())
paper = [[0]*n for _ in range(m)]

for i in range(m):
    ok = list(map(int,input().split()))
    paper[i] = ok

def bfs(paper, y, x):
    dy = [0, 0, 1, -1]
    dx = [1, -1, 0, 0]
    queue = deque([(y, x)])
    paper[y][x] = 0  # 시작 지점을 방문 처리
    size = 1

    while queue:
        y, x = queue.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < m and 0 <= nx < n and paper[ny][nx] == 1:
                paper[ny][nx] = 0  # 방문 처리
                queue.append((ny, nx))
                size += 1
    return size

size_list = []

for i1 in range(m):
    for i2 in range(n):
        if paper[i1][i2] == 1:
            paper[i1][i2] = 0
            size_list.append(bfs(paper,i1,i2))

size_list.sort(reverse=True)
if size_list:
    print(len(size_list))
    print(size_list[0])
else:
    print(0)
    print(0)