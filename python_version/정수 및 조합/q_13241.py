def gcd(a, b) :
  if b == 0 :
    return a
  else :
    # A, B를 교체하여 기존 A자리에 B를 인풋, B자리에는 A%B인 나머지값을 인풋시킨다.
    return gcd(b, a % b)
A, B = map(int, input().split())

# A * B에서 최대공약수인 A를 나누면 최소공배수가 도출됨.
res = A * B // gcd(A, B)
print(res)