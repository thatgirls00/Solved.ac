n = int(input())
m = 1234567891
r = 31
k = input()

res = 0

for i in range(len(k)):
    num = ord(k[i]) - 96
    res += num * (r ** i)

print(res % m)