N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()           # A를 오름차순으로 정렬
B_sorted = sorted(B, reverse=True)  # B를 내림차순으로 정렬하여 B_sorted에 저장

total = 0
for i in range(N):
    total += A[i] * B_sorted[i]

print(total)
