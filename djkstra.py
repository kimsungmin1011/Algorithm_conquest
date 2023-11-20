import heapq


def dijkstra(graph, start):
    # 그래프의 정점 수
    num_vertices = len(graph)

    # 시작 정점으로부터의 최단 거리 배열 초기화
    distance = [float("inf")] * num_vertices
    distance[start] = 0

    # 우선순위 큐를 사용하여 정점을 관리
    priority_queue = [(0, start)]

    while priority_queue:
        # 현재까지의 최단 거리와 현재 정점을 가져옴
        current_dist, current_vertex = heapq.heappop(priority_queue)

        # 현재 정점에서 갈 수 있는 모든 인접 정점을 순회
        for neighbor, weight in graph[current_vertex]:
            distance_through_current = current_dist + weight

            # 현재까지의 거리가 더 짧으면 업데이트하고 큐에 추가
            if distance_through_current < distance[neighbor]:
                distance[neighbor] = distance_through_current
                heapq.heappush(priority_queue, (distance[neighbor], neighbor))

    return distance


# 그래프를 인접 리스트로 표현
graph = [
    [(1, 10), (2, 5)],
    [(0, 10), (2, 15), (3, 5)],
    [(0, 5), (1, 15), (3, 10)],
    [(1, 5), (2, 10)],
]

start_vertex = 0  # 시작 정점

result = dijkstra(graph, start_vertex)
print("시작 정점으로부터의 최단 거리 배열:", result)
