n = int(input())
lst = []

for i in range(n):
    k = int(input())
    if k == 0:
        lst.pop()
    else:
        lst.append(k)

print(sum(lst))
