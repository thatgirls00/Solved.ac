import sys
input = sys.stdin.readline

n, x = map(int, input().split())

if (not (1 <= x <= n <= 250000)):
    exit()
lst = list(map(int, input().split()))

if max(lst) == 0:
    print("SAD")
else:
    lst_num = sum(lst[0:x])
    value = lst_num
    cnt = 1

    for i in range(x, n):
        value -= lst[i-x]
        value += lst[i]
        if value > lst_num:
            lst_num = value
            cnt = 1
        elif value == lst_num:
            cnt += 1
    print(lst_num)
    print(cnt)