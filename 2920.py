a = list(map(int,input().split()))

if a == sorted(a): # 오름차순 정렬이면 ascending
    result = "ascending"
elif a == sorted(a, reverse=True): # 내림차순 정렬이면 descending
    result = "descending"
else: # 둘다 아니라면 mixed
    result = "mixed"

print(result)
