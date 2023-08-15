import sys

N, M = map(int, sys.stdin.readline().split())

wprice = []
nprice = []
money = 0

for i in range(M):
    q, r = map(int, sys.stdin.readline().split())
    wprice.append(q)
    nprice.append(r)

wprice.sort()
nprice.sort()

while N > 0:
    if N >= 6:
        # 6줄 패키지의 가격과 낱개로 6개를 살 때의 가격을 비교
        money += min(wprice[0], nprice[0] * 6)
        N -= 6
    else:
        # 줄이 6개 미만일 때, 6개 패키지의 가격과 낱개로 N개를 살 때의 가격을 비교
        money += min(wprice[0], nprice[0] * N)
        N = 0  # 모든 줄을 채웠으므로 0으로 설정

print(money)
