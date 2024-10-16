def gcd(a, b):
    while b != 0:
        c = a%b
        a = b
        b = c
    return a
n = int(input())
number_list = []
gcd_list = []
gcd_ans = []

for _ in range(n):
    number_list.append(int(input()))

#x = a * gcd, y = b * gcd일 때 x - y = (a - b) * gcd이므로 두수의 차를 구한다.
for i in range(len(number_list)):
  gcd_list.append(abs(number_list[i] - number_list[i - 1]))
N = gcd_list[-1]
for i in range(len(number_list) - 1):
  N = gcd(N, gcd_list[i])
for i in range(2, int(N ** 0.5) + 1):
    if N % i == 0:
        gcd_ans.append(i)
        gcd_ans.append(N // i)
gcd_ans.append(N)
# 3. 결과는 정렬되어 산출
gcd_ans = sorted(list(set(gcd_ans)))
for i in gcd_ans:
    print(i, end = ' ')