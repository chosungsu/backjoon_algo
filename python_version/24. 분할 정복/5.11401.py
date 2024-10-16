import sys

input = sys.stdin.readline

N, K = map(int, input().split())
p = 1000000007
# nCk 형태의 이항계수를 구하는 문제
# 점화식 기본 형태 : n! / k!(n-k)!
# 페르마의 소정리 : a^p = a(modp) => a^p-2 = a^-1(modp) 를 이용
# 점화식을 변형 : n!*((n-k)!k!)^-1%p

# factorial with p
def factorial(N):
    n = 1
    for i in range(2, N+1):
        n = (n * i) % p
    return n
def pow(a, b):
    if b == 0:
        return 1
    if b == 1:
        return a % p
    tmp = pow(a, b//2)
    if b % 2== 0:
        return tmp*tmp%p
    else:
        return tmp*tmp*a%p

first = factorial(N)
second = factorial(N-K) * factorial(K)
print(first * pow(second, p-2) % p)