import sys
input = sys.stdin.readline

m, n = map(int, input().split())
add = {}

for _ in range(m):
    site, ps = input().split()
    add[site] = ps

for _ in range(n):
    print(add[input().rstrip()])
