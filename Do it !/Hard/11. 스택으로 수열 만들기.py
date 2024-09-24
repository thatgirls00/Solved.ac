n = int(input())
a = [0] * n

for i in range(n):
    a[i] = int(input())

stack = []
num = 1
res = True
ans = ""

for i in range(n):
    su = a[i]
    if su >= num:
        while su >= num:
            stack.append(num)
            num += 1
            ans += "+\n"
        stack.pop()
        ans += "-\n"
    else:
        n = stack.pop()
        if n > su:
            print("NO")
            res = False
            break
        else:
            ans += "-\n"

if res:
    print(ans)