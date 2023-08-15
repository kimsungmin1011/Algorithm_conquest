from collections import deque
import sys

# 명령의 수 N을 입력받음
N = int(sys.stdin.readline())
queue = deque()

for _ in range(N):
    command = sys.stdin.readline().split() # input()에 비해 빠른 속도, input 사용하면 시간초과

    # 각 명령에 따른 동작 수행
    if command[0] == 'push':
        queue.append(command[1])
    elif command[0] == 'pop':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.popleft())
    elif command[0] == 'size':
        print(len(queue))
    elif command[0] == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif command[0] == 'front':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    elif command[0] == 'back':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])
