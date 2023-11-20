# 정점의 개수 N 입력 받기
N = int(input())

# 인접 행렬 초기화
graph = []
for _ in range(N):
    row = list(map(int, input().split()))
    graph.append(row)

# 플로이드-와샬 알고리즘
for k in range(N):
    for i in range(N):
        for j in range(N):
            # i에서 j로 가는 경로가 존재하는 경우
            if graph[i][k] == 1 and graph[k][j] == 1:
                graph[i][j] = 1

# 결과 출력
for row in graph:
    print(" ".join(map(str, row)))
