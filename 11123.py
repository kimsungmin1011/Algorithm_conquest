from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
T = int(input())
for _ in range(T):
    H, W = map(int, input().split())
    farm = [[] for _ in range(H)]
    visit = [[False] * W for _ in range(H)]
    for i in range(H):
        line = list(input())
        for i2 in line:
            farm[i].append(i2)

    def bfs(x, y):
        queue = deque([(x, y)])
        while queue:
            x, y = queue.popleft()
            visit[x][y] = True
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if (
                    0 <= nx < H
                    and 0 <= ny < W
                    and visit[nx][ny] == False
                    and farm[nx][ny] == "#"
                ):
                    queue.append((nx, ny))
                    visit[nx][ny] = True

    count = 0
    for i in range(H):
        for i2 in range(W):
            if farm[i][i2] == "#" and visit[i][i2] == False:
                bfs(i, i2)
                count += 1

    print(count)
