from collections import deque
import sys

n = int(sys.stdin.readline())

dq = deque()

for _ in range(n):
    s = sys.stdin.readline().split()
    if s[0] == 'push_front':
        dq.appendleft(s[1])
    elif s[0] == 'push_back':
        dq.append(s[1])
    elif s[0] == 'pop_front':
        if dq:
            print(dq.popleft())
        else:
            print(-1)
    elif s[0] == 'pop_back':
        print(dq.pop()) if dq else print(-1)
    elif s[0] == 'size':
        print(len(dq))
    elif s[0] == 'empty':
        if len(dq) == 0:
            print(1)
        else:
            print(0)
    elif s[0] == 'front':
        if len(dq) != 0:
            print(dq[0])
        else:
            print(-1)
    elif s[0] == 'back':
        if len(dq) != 0:
            print(dq[-1])
        else:
            print(-1)
