n = int(input())

for _ in range(n):
    k = int(input())
    a, b = 1, 0
    for i in range(k): # 0은 1이 호출된 횟수만큼, 1은 0과 1이 호출된 합만큼 출력됨
        a, b = b, a+b
    print(a,b)