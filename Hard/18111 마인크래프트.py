# 1. 시간 초과

'''
import sys

n, m, b = map(int, sys.stdin.readline().split())
g = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
answer = sys.maxsize
idx = 0

#0층부터 256층까지 반복
for target in range(257):
    max_target, min_target = 0, 0

    #반복문을 통해 블록을 확인
    for i in range(n):
        for j in range(m):

            #블록이 층수보다 더 크면
            if g[i][j] >= target:
                max_target += g[i][j] - target

            else:
                min_target += target - g[i][j]

    #블록을 뺀 것과 원래 있던 블록의 합과 블록을 더한 값을 비교
    #블록을 뺸 것과 원래 있던 블록의 합이 더 커야 층을 만들기 가능하다
    if max_target + b >= min_target:
        #시간 초를 구하고 최저 시간과 비교
        if min_target + (max_target * 2) <= answer:
            #0부터 256층까지 비교하므로 업데이트 될수록 고층의 최저시간
            answer = min_target + (max_target * 2) #최저시간
            idx = target #층수

print(answer, idx)

'''

# 2. Retry

import sys

input = sys.stdin.readline

n, m, b = map(int, input().split())
a = []
height = [0 for _ in range(257)]
result_time = sys.maxsize
result_height = 0

for _ in range(n):
    buff = list(map(int, input().split()))
    a.append(buff)

for r in range(n):
    for c in range(m):
        height[a[r][c]] += 1

for i in range(257):
    create_count = 0
    delete_count = 0

    for j in range(257):
        if i >= j:
            create_count += (i - j) * height[j]
        else:
            delete_count += (j - i) * height[j]

    if create_count - delete_count <= b:
        if create_count + delete_count * 2 <= result_time:
            result_time = create_count + delete_count * 2
            result_height = i

print(result_time, result_height)
