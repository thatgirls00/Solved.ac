a, b, v = map(int, input().split())

n = (v - b) / (a - b)
if n == int(n):
    print(int(n))
else:
    print(int(n) + 1)
