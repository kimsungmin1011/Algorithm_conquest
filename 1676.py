n = int(input())

result = 1
for i in range(1,n+1):
    result *= i

result = str(result)
result = result[::-1]


number = 0

for i in range(len(result)):
    if result[i] == '0':
        number += 1
    else:
        break

print(number)