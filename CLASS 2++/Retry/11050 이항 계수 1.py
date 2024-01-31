# 1

'''
from math import factorial
n, k = list(map(int, input().split()))

print(factorial(n) // (factorial(k) * factorial(n-k)))
'''

# 2
n, k = map(int, input().split())

def factorial(num):
    res = 1
    for i in range(2, num+1):
        res *= i
    return res

print(factorial(n) // (factorial(n-k) * factorial(k)))
