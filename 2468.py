from collections import deque

n = int(input())

graph = []

for i in range(n):
    graph.append(list(map(int,input().split())))

max_level = 0
for i in range(n):
    if max(graph[i]) > max_level:
        max_level = max(graph[i])

safe_list = []
for level in range(max_level):
    visited = [[False]*n for _ in range(n)] # 매번 탐색마다 visited 초기화
    def bfs(x,y,graph):
        queue = deque([(x,y)])
        nx = [1,-1,0,0]
        ny = [0,0,1,-1]
        while queue:
            x,y = queue.popleft()
            for i in range(4):
                dx = x + nx[i]
                dy = y + ny[i]
                if 0<=dx<n and 0<=dy<n and graph[dy][dx] > level and visited[dy][dx] == False:
                    visited[dy][dx] = True
                    queue.append((dx,dy))
    
    safe_areas = 0
    for i3 in range(n):
        for i4 in range(n):
            if graph[i3][i4] > level and visited[i3][i4] == False:
                bfs(i4,i3,graph) # bfs 함수 호출
                visited[i3][i4] = True
                safe_areas +=1
    safe_list.append(safe_areas)
print(max(safe_list))