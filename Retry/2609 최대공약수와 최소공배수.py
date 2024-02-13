# 1번 풀이
    # math 모듈 사용
'''
import math
a, b = map(int, input().split())
print(math.gcd(a, b))
print(math.lcm(a, b))
'''

# 2번 풀이
    # 유클리드 호제법 사용
a, b = map(int, input().split())
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def lcm(a, b):
    res = (a * b) // gcd(a, b)
    return res

print(gcd(a, b))
print(lcm(a, b))



