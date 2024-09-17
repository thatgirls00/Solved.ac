n = int(input())
cnt, sum = 0, 0
start, end = 0, 0

while end <= n:
    if sum < n:
        end += 1
        sum += end
    elif sum > n:
        sum -= start
        start += 1
    else:
        cnt += 1
        end += 1
        sum += end

print(cnt)
