# 1. 오류
'''
n, m = map(int, input().split())

res = []
cnt = []

for i in range(n):
    res.append(input())

for j in range(n-7):
    for k in range(m-7): #8*8로 자르기 위해, -7을 해준다
        w_index = 0 #흰색으로 시작
        b_index = 0 #검은색 시작
        for a in range(j, j+8): #시작지점
            for b in range(k, k+8): #시작지점
                if (a+b) % 2 == 0: #짝수일 경우
                    if res[a][b] != 'B': #W가 아니면, 즉 B이면
                        b_index += 1 #W로 칠하는 갯수
                    elif res[a][b] != 'W':
                        w_index += 1
                else:
                    if res[a][b] != 'W': #W가 아니면, 즉 B이면
                        b_index += 1 #B로 칠하는 갯수
                    elif res[a][b] != 'B':
                        w_index += 1

    cnt.append(b_index) #b로 시작할 때 경우의 수
    cnt.append(w_index) #w로 시작할 때 경우의 수

print(min(cnt))
'''

# 2. Retry

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = [list(input().rstrip()) for _ in range(n)]
result = sys.maxsize

for r in range(n-7):
    for c in range(m-7):
        case_white = 0
        case_black = 0
        for i in range(r, r+8):
            for j in range(c, c+8):
                if (i+j) % 2 == 0:
                    if a[i][j] == 'W':
                        case_black += 1
                    else:
                        case_white += 1
                else:
                    if a[i][j] == 'W':
                        case_white += 1
                    else:
                        case_black += 1

        result = min(result, case_white, case_black)

print(result)


