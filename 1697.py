from collections import deque

def bfs(N, K):
    # 큐를 선언하고, 시작점 N을 추가합니다.
    q = deque([(N, 0)])  # (위치, 시간)
    
    # 0~100000까지의 위치를 방문했는지 체크하는 리스트
    visited = [False] * 100001
    visited[N] = True
    
    while q:
        pos, time = q.popleft()
        
        # 동생의 위치에 도달한 경우
        if pos == K:
            return time
        
        # 걷기: X-1 또는 X+1
        for next_pos in [pos-1, pos+1]:
            if 0 <= next_pos <= 100000 and not visited[next_pos]:
                visited[next_pos] = True
                q.append((next_pos, time + 1))
        
        # 순간이동: 2*X
        next_pos = pos * 2
        if 0 <= next_pos <= 100000 and not visited[next_pos]:
            visited[next_pos] = True
            q.append((next_pos, time + 1))

N, K = map(int, input().split())
print(bfs(N, K))
