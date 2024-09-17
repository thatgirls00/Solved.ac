n = int(input())

for i in range(n):
    lst = list(input())
    score = 0
    sum = 0
    for ox in lst:
        if ox == "O":
            score += 1
            sum += score
        else:
            score = 0
    print(sum)
