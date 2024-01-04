n = []

for _ in range(10):
    a = int(input())
    n.append(a % 42)

print(len(set(n))) #set(), 집합을 사용하여 서로 다른 값의 개수를 구하려면 중복을 제거

