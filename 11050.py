n,m=map(int,input().split())
gob = 1
no = 1
takari = 1
for i in range(1,n+1):
    gob *= i

for i in range(1,m+1):
    no *= i

for i in range(1,n-m+1):
    takari *= i

result = int(gob/(no*takari))
print(result)