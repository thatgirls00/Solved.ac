n = int(input())
lst = []

for i in range(n):
    age, name = map(str, input().split())
    age = int(age)
    lst.append((age, name))

lst.sort(key = lambda x : x[0])

for j in range(0, n):
    print(lst[j][0], lst[j][1])
