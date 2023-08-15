S = int(input())

sum = 0
n = 0

while sum < S:
    n += 1
    sum += n

if sum == S:
    print(n)
else:
    print(n-1)
