import sys

k = int(input())

for i in range(k):
    m, n = map(int, sys.stdin.readline().split())
    print(m+n)
