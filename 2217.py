n = int(input())
list = []
for i in range(n):
    a = int(input())
    list.append(a)
list.sort()
print(list[0]*n)