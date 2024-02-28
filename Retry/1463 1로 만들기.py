n = int(input())

dp = [0] * (n+1)

for i in range(2, n+1):
    dp[i] = dp[i-1] + 1

    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2]+1)
    if i % 3 == 0: #elif 사용하지 않고 if 사용을 통해 세 연산을 다 거침
        dp[i] = min(dp[i], dp[i//3]+1)

print(dp[n])
