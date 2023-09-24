import sys

input = sys.stdin.readline

# 부호가 '-' or '+' 가 존재하지만 '-'기준으로 split하는 것이 더 깔끔하다.
strs = input().split('-')
nums = []

for s in strs:
    sum = 0
    tmp = s.split('+')
    for t in tmp:
        sum += int(t)
    nums.append(sum)

# '-'기준으로 먼저 split했었기 때문에 nums 리스트값들로 빼줄 차례이다.
res = nums[0]
for i in range(1, len(nums)):
    res -= nums[i]
print(res)