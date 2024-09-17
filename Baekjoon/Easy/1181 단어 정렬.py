# 첫 번째 풀이

'''
n = int(input())
lst = []

for i in range(n):
    lst.append(input())

lst = list(set(lst))
lst.sort()
lst.sort(key = len)

for i in lst:
    print(i)
'''

# 두 번째 풀이 (리스트 컴프리헨션. 언패킹 사용해서 코드 최적화)

n = int(input())
a = [input() for _ in range(n)]
a = list(set(a))

a.sort()
a.sort(key = lambda x: len(x))

print(*a, sep = '\n')
