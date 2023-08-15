n = int(input())

data = []

for i in range(n):
    age, name = input().split()
    data.append((int(age), name))  # 나이를 int로 변환

data.sort(key=lambda x: x[0])  # 나이만 고려하여 정렬

for i in data:
    print(i[0], i[1])