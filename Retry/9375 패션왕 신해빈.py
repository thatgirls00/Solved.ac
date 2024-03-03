import sys
input = sys.stdin.readline

n = int(input())
for i in range(n):
    t = int(input())
    clothes = {}
    for j in range(t):
        cn, ct = input().split()

        if ct not in clothes.keys():
            clothes[ct] = 1
        else:
            clothes[ct] += 1

    ans = 1
    for i in clothes:
        ans *= (clothes[i]+1)
    print(ans-1)
