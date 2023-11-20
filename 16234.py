from collections import deque

# 입력: 국가의 수(n), 국경선을 열 수 있는 인구 차이의 최소(l) 및 최대(r) 값
n, l, r = map(int, input().split())
# 2차원 배열 A에 각 나라의 인구 수를 입력받음
A = [list(map(int, input().split())) for _ in range(n)]

# 방향 벡터 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


# BFS 함수 정의
def bfs(i, j):
    queue = deque()
    union = []
    queue.append((i, j))
    union.append((i, j))

    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            # 경계 내에 있고 방문하지 않은 국가를 검사
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
                # 인구 차이가 l과 r 사이일 경우 연합에 추가
                if l <= abs(A[nx][ny] - A[x][y]) <= r:
                    visited[nx][ny] = 1
                    queue.append((nx, ny))
                    union.append((nx, ny))
    return union


result = 0  # 이동 횟수를 카운트하는 변수
while True:
    # 방문 여부를 체크하는 2차원 배열 초기화
    visited = [[0 for _ in range(n)] for _ in range(n)]
    flag = 0  # 연합이 형성되었는지를 체크하는 플래그
    for i in range(n):
        for j in range(n):
            # 방문하지 않은 국가에서 BFS 탐색 시작
            if visited[i][j] == 0:
                visited[i][j] = 1
                country = bfs(i, j)

                # 연합이 형성된 경우
                if len(country) > 1:
                    flag = 1
                    people = sum(A[x][y] for x, y in country) // len(country)

                    # 연합 내 모든 국가의 인구를 평균으로 조정
                    for x, y in country:
                        A[x][y] = people

    # 연합이 하나도 형성되지 않았으면 루프 종료
    if flag == 0:
        print(result)
        break

    # 하루가 지날 때마다 result를 1씩 증가시킴
    result += 1
