# 1. 시간 초과
'''
n = int(input())
lst = []

for i in range(n):
    lst.append(int(input()))

for i in sorted(lst):
    print(i)
'''

#2번 풀이

import sys
input = sys.stdin.readline

n = int(input())
a = sorted([int(input()) for i in range(n)])

print(*a, sep = "\n")
