n,a=map(int,input().split())
number=list(map(int,input().split()))
max_sum = 0

for i in range(0, n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            current_sum = number[i] + number[j] + number[k]
            if current_sum <= a and current_sum > max_sum:
                max_sum = current_sum

print(max_sum)