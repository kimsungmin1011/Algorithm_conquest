from collections import deque

# 입력 받기
A, B, N, M = map(int, input().split())

# 방문 여부를 기록하는 리스트 초기화
visited = [False] * 100001

def bfs(n, m):
    count = 0
    queue = deque([(n, count)])
    
    while queue:
        n, count = queue.popleft()
        if n == m:
            return count
        # 이동 가능한 위치를 계산하고 범위 내에 있으며 방문하지 않은 경우 큐에 추가
        for next_n in [n+1, n-1, n*A, n+A, n-A, n*B, n+B, n-B]:
            if 0 <= next_n <= 100000 and not visited[next_n]:
                visited[next_n] = True
                queue.append((next_n, count + 1))
    
result = bfs(N, M)
print(result)
