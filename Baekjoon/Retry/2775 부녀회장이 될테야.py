T = int(input())

for i in range(T):
    h = int(input())
    w = int(input())
    lst = [j for j in range(1, w+1)]

    for k in range(1, h+1):
        for l in range(1, w):
            lst[l] += lst[l-1]
    print(lst[w-1])
