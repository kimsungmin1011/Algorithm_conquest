from collections import deque

a, b = map(int, input().split())

queue = deque(range(1,a+1))
stack = []

for _ in range(a):
    queue.rotate(-b + 1)  # b번째 요소를 왼쪽으로 이동
    stack.append(queue.popleft())  # b번째 요소를 제거하고 stack에 추가

print('<' + ', '.join(map(str, stack)) + '>') # list 내부 요소들 꺼내서 사이사이에 쉼표 넣는 방법