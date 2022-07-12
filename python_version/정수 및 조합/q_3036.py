def gcd(a, b):
    while(b != 0):
        n = a%b
        a = b
        b = n
    return a
#1. 반복할 횟수 읽기
n = int(input())
#2. 반지름을 모두 읽고 리스트에 반영
li = list(map(int, input().split()))
#3. 최대공약수를 구하여 첫번째 반지름과 각각의 반지름 사이 기약분수로 표현
for i in range(1, n):
    g = gcd(li[0], li[i])
    print('{0}/{1}'.format(li[0]//g, li[i]//g))