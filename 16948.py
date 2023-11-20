from collections import deque

N = int(input())
r1, c1, r2, c2 = map(int, input().split())
visited = [[False] * N for _ in range(N)]

dx = [-2, -2, 0, 0, 2, 2]
dy = [-1, 1, -2, 2, -1, 1]


def bfs(x, y):
    queue = deque([(x, y, 0)])
    while queue:
        x, y, count = queue.popleft()
        if x == r2 and y == c2:
            return count
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and visited[ny][nx] == False:
                queue.append((nx, ny, count + 1))
                visited[ny][nx] = True
    return -1


print(bfs(r1, c1))
