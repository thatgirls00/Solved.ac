m, n = map(int, input().split())
lst = list(map(int, input().split()))

s = sum(lst[:n])
answer = s

for i in range(m-n):
    s += lst[i+n] - lst[i]
    if answer < s:
        answer = s

print(answer)
