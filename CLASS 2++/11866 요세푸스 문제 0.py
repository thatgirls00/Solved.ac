import sys

n, k = map(int, sys.stdin.readline().split())

idx = 0
que = [i for i in range(1, n+1)]
res = []

while que:
    idx += k -1
    if idx >= len(que):
        idx %= len(que)
    res.append(str(que.pop(idx)))

print("<", ", ".join(res), ">", sep="")