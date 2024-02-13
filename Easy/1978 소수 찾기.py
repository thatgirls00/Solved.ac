n = int(input())

lst = list(map(int, input().split()))
res = 0

for i in lst:
    err = 0
    if i > 1:
        for j in range(2, i):
            if i % j == 0:
                err += 1
        if err == 0:
            res += 1

print(res)
