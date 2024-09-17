m, n = map(int, input().split())

a = set()
for i in range(m):
    a.add(input())

b = set()
for i in range(n):
    b.add(input())

res = sorted(list(a&b))

print(len(res))

for i in res:
    print(i)
