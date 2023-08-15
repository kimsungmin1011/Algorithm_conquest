N = int(input())
P = list(map(int, input().split()))

# 사람들이 돈을 인출하는 시간을 오름차순으로 정렬
P.sort()

result = 0
wait_time = 0
for time in P:
    wait_time += time
    result += wait_time

print(result)