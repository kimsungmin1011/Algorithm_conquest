def d(n):
    # n과 n의 각 자리수를 더하는 함수
    return n + sum(map(int, str(n)))

# 1부터 10000까지의 숫자 중에서 셀프 넘버가 아닌 숫자를 담을 set
not_self_numbers = set()

for i in range(1, 10001):
    not_self_numbers.add(d(i))

# 1부터 10000까지의 숫자 중에서 not_self_numbers에 없는 숫자가 셀프 넘버
for i in range(1, 10001):
    if i not in not_self_numbers:
        print(i)
