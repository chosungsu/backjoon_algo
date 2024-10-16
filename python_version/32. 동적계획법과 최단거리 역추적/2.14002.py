import sys

input=sys.stdin.readline
lenA = int(input())
data = list(map(int, input().split()))
dp = [1] * (lenA+1)

for i in range(len(data)):
    for j in range(i):
        if data[j] < data[i]:
            dp[i] = max(dp[i], dp[j]+1)
# 수열 중 가장 길게 증가하는 부분을 max로 추출
print(max(dp))
x = max(dp)

result = []
for i in range(lenA-1, -1, -1):
    if dp[i] == x:
        result.append(data[i])
        x -= 1
result.reverse()
for r in result:
    print(r, end=' ')