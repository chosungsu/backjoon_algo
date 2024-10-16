a, b = map(int, input().split())
time = int(input()) 
a += time // 60
b += time % 60
if b >= 60:
    a += 1
    b -= 60
if a >= 24:
    a -= 24
print(a,b)