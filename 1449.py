# 입력값 받기
n, l = map(int, input().split())
data = list(map(int, input().split()))

# 물이 새는 위치 오름차순 정렬
data.sort()

# 테이프를 처음 붙이는 시작지점
start = data[0] - 0.5
# 필요한 테이프의 개수
count = 1

# 물이 새는 곳의 위치를 차례대로 받으면서
for location in data[1:]:
    # 테이프를 붙이는 범위 내에 물이 새는 곳의 위치가 있다면
    if start <= location <= (start + l):
        # 기존 테이프 사용
        continue
    # 기존의 테이프로 붙이지 못한다면
    else:
        # 새 테이프를 사용하고 테이프 개수 추가
        count += 1
        # 새로운 물이 새는 지점에 대해 테이프를 붙이는 시작 지점 업데이트
        start = location - 0.5

# 필요한 테이프의 개수 출력
print(count)
