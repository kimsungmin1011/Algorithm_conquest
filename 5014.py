from collections import deque

F,S,G,U,D = map(int,input().split())

def bfs(top,start,end,up,down):
    visited = [False] * (F + 1)  # 1부터 F까지의 층을 방문했는지 표시 (무한루프 방지)
    visited[start] = True
    queue = deque([(start,0)])
    while queue:
        start,level = queue.popleft()

        if start == end:
            return level
        
        if start+up<=top and visited[start+up] == False:
            queue.append((start+up,level+1))
            visited[start+up] = True

        if start-down>0 and visited[start-down] == False:
            queue.append((start-down,level+1))
            visited[start-down] = True

    return "use the stairs" # level이 있으면 이미 앞에서 출력됨. 끝까지 탐색하고 불가능하면 return

print(bfs(F, S, G, U, D))