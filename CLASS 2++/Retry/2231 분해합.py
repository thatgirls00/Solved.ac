n = int(input())
result = 0

for i in range(n):
    cnt = i + sum(map(int, str(i)))
    if cnt == n:
        result = i
        break

print(result)
