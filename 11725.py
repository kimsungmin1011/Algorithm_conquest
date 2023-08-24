from collections import deque

n = int(input())
tree = [[] for _ in range(n + 1)]

# 트리 정보 입력 받기
for _ in range(n - 1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

def bfs(start):
    visited = [False] * (n + 1)
    parents = [0] * (n + 1)
    queue = deque([start])
    visited[start] = True

    while queue:
        current = queue.popleft()

        for node in tree[current]:
            if not visited[node]:
                parents[node] = current
                visited[node] = True
                queue.append(node)

    return parents

parents = bfs(1)

# 2번 노드부터 부모 노드 출력
for i in range(2, n + 1):
    print(parents[i])
