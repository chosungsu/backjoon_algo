N, B = map(int, input().split())
s = ''
ary = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

while N != 0:
    s += str(ary[N%B])
    N //= B

print(s[::-1])