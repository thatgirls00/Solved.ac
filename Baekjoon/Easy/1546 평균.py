n = int(input())
lst = list(map(int, input().split()))

res = []
for i in lst:
    res.append(i / max(lst) * 100)
avg = sum(res) / n
print(avg)
