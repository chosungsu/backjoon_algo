import sys

input = sys.stdin.readline
n = int(input())
num = list(map(int, input().split()))
x = int(input())

cnt = 0

i = 0
j = len(num) - 1

num.sort()

while i < j:
    # 구해야 하는 수식
    temp = num[i] + num[j]
    # 수식이 성립하는 경우
    if temp == x:
        cnt += 1
        i += 1
        j -= 1
    # 수식보다 x 값이 더 클 경우
    # 작은 i를 증가시킨다.
    elif temp < x:
        i += 1
    # 수식이 x 값보다 더 클 경우
    # 큰 j를 감소시킨다.
    else:
        j -= 1

print(cnt)