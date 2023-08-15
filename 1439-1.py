dasom = input()  # 문자열을 그대로 사용
cnt = 0

for i in range(len(dasom)-1):
    if dasom[i] != dasom[i+1]:
        cnt+=1

print((cnt+1)//2)
