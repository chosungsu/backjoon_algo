def gcd(a, b) :
  if b == 0 :
    return a
  else :
    # A, B를 교체하여 기존 A자리에 B를 인풋, B자리에는 A%B인 나머지값을 인풋시킨다.
    return gcd(b, a % b)

N = int(input())
res = 0
# 주어진 위치를 담는 리스트
arr_1 = []
# 위치 간격을 담는 리스트
arr_2 = []

for i in range(N):
    arr_1.append(int(input()))
    if i != 0:
        arr_2.append(abs(arr_1[i] - arr_1[i - 1]))
# 최대공약수를 구하는 부분
gcd_tmp = arr_2[0]
for k in range(1, len(arr_2)):
    gcd_tmp = gcd(gcd_tmp, arr_2[k])
# 처음과 마지막의 위치를 최종 구해진 최대공약수로 나눈 값에 1을 더한 후 전체 개수를 소거함
res = (arr_1[-1] - arr_1[0]) // gcd_tmp + 1 - N
print(res)