def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

n, k = map(int, input().split())
# answer : nCk 형태를 구하면 된다.(factorial algorithm 이용)
print(factorial(n) // (factorial(k) * factorial(n - k)))