N, B = input().split()
ary = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

N = N[::-1]
result = 0

for i,n in enumerate(N):
    result += (int(B)**i)*(ary.index(n))
print(result)