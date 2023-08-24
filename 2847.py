# 레벨의 수 입력받기
N = int(input())

# 각 레벨의 점수를 입력받기
scores = [int(input()) for _ in range(N)]   

# 점수 조절 횟수를 저장할 변수
count = 0

# 뒤에서부터 앞으로 검사
for i in range(N-1, 0, -1):
    if scores[i] <= scores[i-1]:
        # 조절해야 할 차이를 계산
        diff = scores[i-1] - scores[i] + 1
        # 점수 조절
        scores[i-1] -= diff
        # 조절 횟수 카운트
        count += diff

# 결과 출력
print(count)
