n = int(input())
fib = [0, 1]

for i in range(2, n+1):
    num = fib[i-1] + fib[i-2]
    fib.append(num)
print(fib[n])

