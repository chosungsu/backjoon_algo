import sys

input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split(' ')))
arr.sort()

left = 0
right = n-1

answer = abs(arr[left] + arr[right])
final = [arr[left], arr[right]]


while left < right:
    left_val = arr[left]
    right_val = arr[right]

    sum = left_val + right_val
    # 아래 수식으로 변경 이후의 정답이 직전의 정답보다 작을 경우(절댓값 기준)
    # 교체
    if abs(sum) < answer:
        answer = abs(sum)
        final = [left_val, right_val]
        if answer == 0:
          break
    # 음수인 경우 left를 증가
    if sum < 0:
        left += 1
    # 양수인 경우 right를 증가
    else:
        right -= 1

print(final[0], final[1])