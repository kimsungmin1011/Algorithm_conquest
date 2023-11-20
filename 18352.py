from collections import deque
import sys
input = sys.stdin.readline # 시간 초과 해결

n,m,k,x = map(int,input().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
for i in range(m):
    t,y = map(int,input().split())
    graph[t].append(y)

def bfs(k,x,graph,visited):
    queue = deque([(x,0)])
    visited[x] = True
    nodes_at_k = []  # 거리가 k인 모든 노드를 저장할 리스트
    while queue:
        x,count = queue.popleft()
        # 거리가 k인 노드를 nodes_at_k에 추가합니다.
        if count == k:
            nodes_at_k.append(x)

        for i in graph[x]:
            if visited[i] == False:
                visited[i] = True
                queue.append((i,count+1))
    if nodes_at_k:          
        return nodes_at_k
    else:
        return -1

result = bfs(k, x, graph, visited)
if result == -1: # 결과가 -1일 시
    print(-1)
else:
    for i in sorted(result): # 결과가 제대로 나왔을 시
        print(i)
