n = input()
a = 'abcdefghijklmnopqrstuvwxyz'

for i in a:
    if i in n:
        print(n.index(i), end= ' ')
    else:
        print(-1, end = ' ')
