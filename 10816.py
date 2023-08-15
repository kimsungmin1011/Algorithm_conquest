import sys

n = int(sys.stdin.readline())
number = list(map(int,sys.stdin.readline().split()))
m = int(sys.stdin.readline())
guess = list(map(int,sys.stdin.readline().split()))

# 해시 테이블 구현 부분 시작
# 숫자 카드의 각 숫자별 등장 횟수를 dictionary에 저장
num_dict = {} # 여기서 dictionary가 해시 테이블 역할을 합니다.
for num in number:
    if num in num_dict:
        num_dict[num] += 1
    else:
        num_dict[num] = 1
# 해시 테이블 구현 부분 끝

# 결과를 저장할 리스트
result = []

# 주어진 M개의 수에 대해 dictionary에서 해당 숫자의 등장 횟수를 확인
for g in guess:
    if g in num_dict: # 해시 테이블에서 키의 존재를 빠르게 검색
        result.append(str(num_dict[g]))
    else:
        result.append('0')

print(' '.join(result))