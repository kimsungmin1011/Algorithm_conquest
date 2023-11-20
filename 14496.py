from collections import deque

a, b = map(int, input().split())
N, M = map(int, input().split())
ground = [[] for _ in range(N + 1)]
visit = [False] * (N + 1)  # 실수한 지점!!
for i in range(M):
    x, y = map(int, input().split())
    ground[x].append(y)
    ground[y].append(x)


def bfs():
    queue = deque([(a, 0)])
    while queue:
        num, count = queue.popleft()
        visit[num] = True
        if num == b:
            return count
        for i in ground[num]:
            if visit[i] == False:
                queue.append((i, count + 1))
                visit[i] = True
    return -1


print(bfs())
