n = int(input())
lst = []

for i in range(n):
   lst.append(int(input()))
lst1 = sorted(lst)
for i in range(len(lst)):
    print(lst1[i])
