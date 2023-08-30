from collections import deque

# 노드의 개수 입력 받기
n = int(input())
s,e = map(int,input().split())
r = int(input())

# 그래프를 인접 리스트로 표현
graph = [[] for _ in range(n+1)]
for _ in range(r):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(graph, s, e):
    queue = deque([(s, 0)])  # 시작 노드와 그 노드까지의 촌수를 함께 큐에 넣음
    visited = [False] * (n + 1)
    visited[s] = True

    while queue:
        v, relation = queue.popleft()  # 노드와 해당 노드까지의 촌수를 함께 가져옴

        for i in graph[v]:
            if i == e:
                return relation + 1  # 목표 노드를 찾았을 때의 촌수를 반환
            elif not visited[i]:
                visited[i] = True
                queue.append((i, relation + 1))  # 인접 노드와 그 노드까지의 촌수를 함께 큐에 넣음

    return -1

print(bfs(graph,s,e))