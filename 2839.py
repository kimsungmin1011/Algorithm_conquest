N = int(input())

# 5킬로그램 봉지로 최대한 많이 담기
bags_of_5 = N // 5
remaining_kg = N % 5

while bags_of_5 >= 0:
    if remaining_kg % 3 == 0:  # 나머지를 3킬로그램 봉지로 담을 수 있으면
        bags_of_3 = remaining_kg // 3
        print(bags_of_5 + bags_of_3)
        break
    else:
        bags_of_5 -= 1  # 5킬로그램 봉지 하나 줄이기
        remaining_kg += 5  # 줄인 5킬로그램을 3킬로그램 봉지로 채울 수 있는지 확인하기 위해 나머지에 더해줌
else:  # 모든 경우에도 N킬로그램을 만들 수 없는 경우
    print(-1)
