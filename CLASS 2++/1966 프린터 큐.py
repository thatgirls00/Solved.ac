n = int(input())

for i in range(n):
    a, b = map(int, input().split())
    lst = list(map(int, input().split()))
    result = 1

    while lst:
        if lst[0] < max(lst):
            lst.append(lst.pop(0))

        else:
            if b == 0:
                break

            lst.pop(0)
            result += 1

        b = b -1 if b > 0 else len(lst) -1

    print(result)