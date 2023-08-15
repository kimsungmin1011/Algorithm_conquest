from collections import deque
import sys

n = int(input())
deque = deque()

for i in range(n):
    royal = sys.stdin.readline().split()

    if royal[0]=='push_front':
        deque.appendleft(royal[1])

    elif royal[0]=='push_back':
        deque.append(royal[1])
    
    elif royal[0]=='pop_front':
        if len(deque) >0:
            print(deque.popleft())
        else:
            print(-1)
    
    elif royal[0]=='pop_back':
        if len(deque) >0:
            print(deque.pop())
        else:
            print(-1)

    elif royal[0]=='size':
        print(len(deque))
    
    elif royal[0]=='empty':
        if len(deque) == 0:
            print(1)
        else:
            print(0)
    
    elif royal[0]=='front':
        if len(deque)>0:
            print(deque[0])
        else:
            print(-1)
    
    elif royal[0]=='back':
        if len(deque)>0:
            print(deque[-1])
        else:
            print(-1)
