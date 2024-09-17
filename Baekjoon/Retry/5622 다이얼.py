lst = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
n = input()
res = 0

for i in range(len(n)):
    for j in lst:
        if n[i] in j:
            res += lst.index(j)+3

print(res)
