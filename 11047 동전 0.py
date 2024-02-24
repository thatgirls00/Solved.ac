m, n = map(int, input().split())

coins = []

for _ in range(m):
    coins.append(int(input()))
coins.sort(reverse=True)

answer = 0
for i in coins:
    if n >= i:
        answer += n // i
        n %= i
        if n <= 0:
            break

print(answer)
