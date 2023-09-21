def gcd(a, b) :
  if b == 0 :
    return a
  else :
    # A, B를 교체하여 기존 A자리에 B를 인풋, B자리에는 A%B인 나머지값을 인풋시킨다.
    return gcd(b, a % b)
N = 2
arr_1 = list(map(int, input().split()))
arr_2 = list(map(int, input().split()))
res = gcd(arr_1[0] * arr_2[1] + arr_2[0] * arr_1[1], arr_1[1] * arr_2[1])
print((arr_1[0] * arr_2[1] + arr_2[0] * arr_1[1]) // res, arr_1[1] * arr_2[1] // res)