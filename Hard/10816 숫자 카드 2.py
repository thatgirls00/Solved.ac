n = int(input())
c = list(map(int, input().split(' ')))
c.sort()

m = int(input())
t = list(map(int, input().split(' ')))

dic = dict()

for i in c:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

for i in range(m):
    if t[i] in dic:
        print(dic[t[i]], end=' ')
    else:
        print(0, end=' ')
