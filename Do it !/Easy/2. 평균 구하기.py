n = int(input())
lst = list(map(int, input().split()))

max = max(lst)
sum = sum(lst)

print(sum * 100 / max / int(n))
