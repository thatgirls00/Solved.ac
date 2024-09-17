m, n = input().split()

m = int(m[::-1])
n = int(n[::-1])

if m > n:
    print(m)
else:
    print(n)
