import sys
from collections import Counter

cnt = int(sys.stdin.readline())
num = []

for i in range(cnt):
    n = int(sys.stdin.readline())
    num.append(n)

if cnt == 1:
    print(num[0], num[0], num[0], 0, sep='\n')

else:
    num.sort()
    mode = Counter(num).most_common(2)

    print(round(sum(num)/cnt))
    print(num[cnt//2])
    if mode[0][1] == mode[1][1]:
        print(mode[1][0])
    else:
        print(mode[0][0])
    print(max(num) - min(num))

