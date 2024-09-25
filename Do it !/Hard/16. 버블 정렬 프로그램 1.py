import sys
input = sys.stdin.readline

n = int(input())
lst = []

for i in range(n):
   lst.append((int(input()), i))

max = 0
sorted_lst = sorted(lst)

for i in range(n):
   if max < sorted_lst[i][1] - i:
      max = sorted_lst[i][1] - i

print(max + 1)
