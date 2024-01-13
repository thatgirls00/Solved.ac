def num(M, N):
    for i in range(M, N + 1):
        if i > 1:
            s = True
            for j in range(2, int(i ** 0.5) + 1):
                if i % j == 0:
                    s = False
                    break
            if s:
                print(i)

M, N = map(int, input().split())
num(M, N)
