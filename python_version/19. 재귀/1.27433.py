N = int(input())

res = 1
if N == 0:
    print(res)
else:
    for i in range(2, N+1):
        res *= i
    print(res)