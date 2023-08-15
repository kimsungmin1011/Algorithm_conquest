s = input().split('-')
result = sum(map(int, s[0].split('+')))  # 첫 번째 항목에 대해 '-'를 기준으로 집합을 나눈 뒤 첫번째 집합에서 '+'를 기준으로 숫자들 split하고 합산 (result 선언)

for i in s[1:]:
    result -= sum(map(int, i.split('+')))  # 이후 항목들에 대해 '-'를 기준으로 나눈 각각의 집합에서 '+'를 기준으로 숫자들 split하고 합산한 뒤 결과에서 뺌

print(result)