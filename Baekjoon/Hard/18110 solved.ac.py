import sys

def roundup(n):
    if (n - int(n)) >= 0.5:
        return int(n) + 1
    else:
        return int(n)

k = int(sys.stdin.readline().rstrip())

if k == 0:
    print(0)

else:
    arr = []

    for i in range(k):
        arr.append(int(sys.stdin.readline().rstrip()))

    arr.sort()
    l = roundup(k * 0.15)

    print(roundup(sum(arr[l:k-l]) / len(arr[l:k-l])))
