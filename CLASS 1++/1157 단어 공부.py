s = input().upper()
lst = list(set(s))
res = []

for i in lst:
    res.append(s.count(i))

if res.count(max(res)) > 1:
    print("?")
else:
    print(lst[(res.index(max(res)))])