n, m = map(int, input().split())

arr = [[0 for j in range(m)] for i in range(n)]

for i in range(n):
    ra = list(map(int, input().split()))
    for j in range(m):
        arr[i][j] += ra[j]

for p in range(n):
    rb = list(map(int, input().split()))
    for q in range(m):
        arr[p][q] += rb[q]

for k in arr:
    for l in k:
        print(l, end=' ')
    print()