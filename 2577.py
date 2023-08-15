# 세 숫자를 입력받아 곱한 결과를 문자열로 변환
result = str(int(input()) * int(input()) * int(input()))

# 0부터 9까지의 각 숫자에 대해
for i in range(10):
    # 결과 문자열에서 해당 숫자가 몇 번 등장하는지 세고 출력
    print(result.count(str(i)))
