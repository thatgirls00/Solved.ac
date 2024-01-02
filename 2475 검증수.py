a = map(int, input().split())
res = 0
for i in a:
    res += i*i
print(res % 10)

