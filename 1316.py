# 입력 받는 단어의 개수 N
N = int(input())

# 그룹 단어의 개수를 저장할 변수
count = 0

# N개의 단어에 대하여 반복
for _ in range(N):
    word = input()
    
    # 그룹 단어인지 아닌지 판별하는 변수. 처음에는 True로 가정
    group_word = True
    
    # 이미 방문한 문자들을 저장하는 리스트
    visited = []

    # 단어의 각 문자를 순회하면서 그룹 단어인지 확인
    for i in range(len(word)):
        # 현재 문자가 이전 문자와 다르고, 이미 방문한 문자 리스트에 현재 문자가 있다면 그룹 단어가 아니다.
        if i > 0 and word[i] != word[i-1] and word[i] in visited:
            group_word = False
            break
        
        # 현재 문자를 방문한 문자 리스트에 추가
        visited.append(word[i])

    # 단어가 그룹 단어인 경우 count 증가
    if group_word:
        count += 1

# 그룹 단어의 개수 출력
print(count)