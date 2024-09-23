import sys
input = sys.stdin.readline

n = int(input())
res = 0
a = list(map(int, input().split()))
a.sort()

for k in range(n):
    find = a[k]
    i = 0
    j = n - 1
    while i < j:
        if a[i] + a[j] == find:
            if i != k and j !=k:
                res += 1
                break
            elif i == k:
                i += 1
            elif j == k:
                j -= 1
        elif a[i] + a[j] < find:
            i += 1
        else:
            j -= 1

print(res)