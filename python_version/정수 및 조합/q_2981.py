import math
# 1. 읽어야 할 개수 읽기
t = int(input())
s = []
a = []
gcd = 0
# 2. 리스트에 담기
for i in range(t):
    s.append(int(input()))
    if i == 1:
        gcd = abs(s[1] - s[0])
    gcd = math.gcd(abs(s[i] - s[i - 1]), gcd)
gcd_a = int(gcd ** 0.5)
for i in range(2, gcd_a + 1):
    if gcd % i == 0:
        a.append(i)
        a.append(gcd // i)
a.append(gcd)
# 3. 결과는 정렬되어 산출
a = list(set(a))
a.sort()
for i in a:
    print(i, end = ' ')