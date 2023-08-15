import sys

n = int(sys.stdin.readline())
a = set(sys.stdin.readline().split()) # 시간 초과 때문에 set() 함수를 이용해서 중복값 제거

m = int(sys.stdin.readline())
b = sys.stdin.readline().split()

for i in range(m):
    if b[i] in a:
        print(1)
    else:
        print(0)