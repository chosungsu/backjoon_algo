a, b = map(int, input().split())
# 최대공약수
def gcd(a, b):
    while b != 0:
        c = a%b
        a = b
        b = c
    return a
# 최소공배수
def lcm(a,b):
    baesu = (a*b) / gcd(a,b)
    return baesu
 
print(gcd(a,b))
print(int(lcm(a,b)))