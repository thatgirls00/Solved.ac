N, M = map(int, input().split())

arr = list(map(int, input().split()))
lst = []

for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            three = arr[i] + arr[j] + arr[k]
            if three > M:
                continue
            else:
                lst.append(three)
print(max(lst))
