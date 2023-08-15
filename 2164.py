from collections import deque

N = int(input())
queue = deque([i for i in range(1, N+1)])

while len(queue) > 1:
    # 제일 위에 있는 카드를 바닥에 버리는 연산
    queue.popleft()
    # 제일 위에 있는 카드를 제일 아래에 있는 카드 밑으로 옮기는 연산
    queue.append(queue.popleft())

print(queue[0])