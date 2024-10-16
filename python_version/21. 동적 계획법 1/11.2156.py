n = int(input())
arr = [int(input()) for _ in range(n)]
dp = [0] * (n)
# 조건
# 1. 포도주 잔은 원래 위치로 돌려놓는다.
# 2. 연속해서 3잔을 마실 수 없다.

# 따라서 2잔 연속으로 마시는 경우까지는 하드코딩, 이후는 점화식 사용
# 점화식 설명
# arr[i]는 마지막 잔으로 보고 dp[i - 2]는 마지막에서 두번째 전 잔까지 마신 경우
# dp[i - 3]은 arr[i], arr[i - 1]과 dp[i - 2]는 연속되므로 한 잔 전까지 마신 경우
# dp[i - 1]은 마지막 잔을 마시지 않은 경우
if n >= 1:
    dp[0] = arr[0]
if n >= 2:
    dp[1] = arr[0] + arr[1]
if n >= 3:
    dp[2] = max(arr[2] + arr[1], arr[2] + arr[0], dp[1])
if n >= 4:
    for i in range(3, n):
        dp[i] = max(arr[i] + dp[i - 2], arr[i] + arr[i - 1] + dp[i - 3], dp[i - 1])
print(max(dp))