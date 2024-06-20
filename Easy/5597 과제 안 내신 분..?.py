s = [i for i in range(1, 31)] # 리스트 컴프리헨션

for _ in range(28):
    n = int(input())
    s.remove(n)

print(min(s))
print(max(s))
