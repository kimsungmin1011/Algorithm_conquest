N, M = map(int, input().split())
DNAs = [input() for _ in range(N)]

result = []
hamming_distance_sum = 0

for i in range(M):
    count = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    
    # 모든 DNA의 i번째 문자를 세기
    for dna in DNAs:
        count[dna[i]] += 1

    # 가장 많은 빈도를 갖는 문자를 결과에 추가
    max_char = max(count, key=count.get)
    result.append(max_char)

    # Hamming Distance 계산
    hamming_distance_sum += (N - count[max_char])

print(''.join(result))
print(hamming_distance_sum)
