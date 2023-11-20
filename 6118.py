from collections import deque

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]  # graph의 크기를 N+1로 초기화해야함
visited = [False] * (N + 1)
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

count_dict = [0] * (N + 1)


def bfs():
    queue = deque([(1, 0)])
    while queue:
        x, count = queue.popleft()
        count_dict[x] = count
        visited[x] = True
        for i in graph[x]:
            if visited[i] == False:
                queue.append((i, count + 1))
                visited[i] = True


bfs()

index = 0
distance = count_dict[0]
for i in range(N):
    if count_dict[i + 1] > distance:
        distance = count_dict[i + 1]
        index = i + 1

num = 0
for i in range(N + 1):
    if count_dict[i] == distance:
        num += 1

print(index, distance, num)
