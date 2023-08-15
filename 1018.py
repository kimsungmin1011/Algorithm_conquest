n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]

# 체스판의 두 패턴
pattern1 = [
    ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
    ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
    ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
    ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
    ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
    ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
    ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
    ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']
]

pattern2 = [
    ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
    ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
    ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
    ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
    ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
    ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
    ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
    ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B']
]

# 각 패턴과 얼마나 다른지 확인하는 함수
def check_diff(x, y, pattern):
    diff = 0
    for i in range(8):
        for j in range(8):
            if board[x + i][y + j] != pattern[i][j]:
                diff += 1
    return diff

# 모든 8x8 부분에 대해 패턴과의 차이를 구하고 최솟값을 찾기
min_diff = float('inf')
for i in range(n - 7):
    for j in range(m - 7):
        diff1 = check_diff(i, j, pattern1)
        diff2 = check_diff(i, j, pattern2)
        min_diff = min(min_diff, diff1, diff2)

print(min_diff)