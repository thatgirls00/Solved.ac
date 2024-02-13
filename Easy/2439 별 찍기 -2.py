a = int(input())

for i in range(a):
  for j in range(a-i-1):
    print(' ',end ="")
  for k in range(i+1):
    print('*', end="")
  print()
