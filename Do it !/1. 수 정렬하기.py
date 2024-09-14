n = int(input())
lst = []

for i in range(n):
    num = int(input())
    lst.append(num)

lst.sort()

for i in lst:
    print(i)
