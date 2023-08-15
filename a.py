import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline #python은 재귀제한이 걸려있기 때문에 재귀 허용치가 넘어가면 런타임에러를 일으킨다. 따라서 허용 범위를 넓혀준다. 

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)] #graph[0]은 비우기 때문에 n+1로 함
visited = [False] * (n+1)

for _ in range(m): #연결요소 (그래프) 채우기
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

def dfs(v): #연결요소 (그래프) 내부 뒤지고 재귀함수로 계속 반복
    visited[v] = True
    for i in graph[v]:
        if visited[i] == False:
            visited[i] = True
            dfs(i)

count = 0
for i in range(1, n+1):
    if visited[i] == False:
        count+=1
        dfs(i) # 이미 dfs 함수에서 그래프 내부 요소들의 visited를 True로 바꿨기 때문에 연결요소가 완전히 별개인 것에만 count가 추가됨

print(count)