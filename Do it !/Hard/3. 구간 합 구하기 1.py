#hard

import sys

input = sys.stdin.readline # 반복문 여러 줄 입력 받는 상황에서는 반드시 sys 모듈 사용(시간 초과 오류)
a, b = map(int, input().split())
num = list(map(int, input().split()))
sum = [0]
temp = 0

for i in num:
    temp = temp + i
    sum.append(temp)

for i in range(b):
    s, e = map(int, input().split())
    print(sum[e] - sum[s-1])