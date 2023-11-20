from collections import deque

# 사다리와 뱀의 수 입력 받기
n, m = map(int, input().split())

# 사다리 정보 입력 받기
ladders = []
for _ in range(n):
    x, y = map(int, input().split())
    ladders.append((x, y))

# 뱀 정보 입력 받기
snakes = []
for _ in range(m):
    u, v = map(int, input().split())
    snakes.append((u, v))

# 보드판을 1에서 100까지의 숫자로 초기화
board = [i for i in range(101)]

# 사다리와 뱀의 위치를 보드판에 설정
for start, end in ladders:
    board[start] = end
for start, end in snakes:
    board[start] = end


# BFS를 사용하여 최소 주사위 굴림 횟수 계산
def bfs():
    visited = [False] * 101  # 방문한 칸을 기록
    queue = deque([(1, 0)])  # 시작 위치와 주사위 굴림 횟수
    while queue:
        position, throws = queue.popleft()
        if position == 100:  # 100번 칸에 도달한 경우
            return throws
        for i in range(1, 7):  # 주사위의 가능한 모든 결과에 대해
            next_pos = position + i
            if next_pos <= 100 and not visited[next_pos]:
                visited[next_pos] = True
                queue.append((board[next_pos], throws + 1))
    return -1  # 100번 칸에 도달할 수 없는 경우


# 함수 실행
print(bfs())
