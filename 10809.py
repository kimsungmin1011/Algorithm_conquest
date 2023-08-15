# 입력 단어를 받는다.
word = input()

# 각 알파벳의 위치를 저장할 리스트를 초기화한다.
# 단어에 포함되지 않은 알파벳에 대해서는 -1을 저장한다.
alphabet = [-1]*26

# 단어의 각 문자에 대해
for i in range(len(word)):
    # 해당 문자가 처음 등장하는 경우
    if alphabet[ord(word[i]) - ord('a')] == -1:
        # 해당 문자의 위치를 저장한다.
        alphabet[ord(word[i]) - ord('a')] = i

# 각 알파벳의 위치를 공백으로 구분하여 출력한다.
# 이때, 각 위치는 문자열로 변환하여 출력한다.
print(" ".join(map(str, alphabet)))
