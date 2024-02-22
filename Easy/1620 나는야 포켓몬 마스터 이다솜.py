import sys

m, n = map(int, input().split())

dic_int = {}
dic_name = {}

for i in range(m):
    name = sys.stdin.readline().strip()
    dic_int[i] = name
    dic_name[name] = i

for _ in range(n):
    item = sys.stdin.readline().strip()
    if item.isdigit() == True:
        print(dic_int[int(item)-1])
    else:
        print(dic_name[item]+1)
