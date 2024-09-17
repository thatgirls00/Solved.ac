n = int(input())
lst = list(map(int, input().split()))

lst.sort()

res = 0
for i in range(1, n+1):
    res += sum(lst[:i])

print(res)
