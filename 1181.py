n = int(input())

array = []

for i in range(n):
    array.append(input()) # 입력받아서 array에 넣음
    
array=list(set(array)) # set()함수로 중복 단어 제거, list()로 묶어서 리스트로 변환
array.sort(key=lambda x: (len(x),x)) # 첫번째 조건: 단어의 길이, 두번째 조건: 단어 자체(사전 순으로 정렬)

for word in array:
    print(word)