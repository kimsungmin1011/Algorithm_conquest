N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]

count = 0

# 동전들을 내림차순으로 정렬
coins.sort(reverse=True)

for coin in coins:
    # 현재 동전으로 만들 수 있는 최대 개수를 구함
    coin_count = K // coin
    count += coin_count
    
    # K를 업데이트
    K -= coin * coin_count

    # K가 0이 되면 종료
    if K == 0:
        break

print(count)
