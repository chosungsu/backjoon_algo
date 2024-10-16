stairs = int(input())
arr = [int(input()) for _ in range(stairs)]

#10 20 15 25 10 20
#마지막은 반드시 밟아야 한다.
#연속으로 세번 밟으면 안된다.
#한칸 혹은 두칸 건너 밟을 수 있다.
#1층, 2층, 3층은 하드코딩이 필요하다.

dp = [0] * (stairs+1)
if stairs >= 1:
    dp[0] = arr[0]
if stairs >= 2:
    dp[1] = arr[0] + arr[1]
if stairs >= 3:
    dp[2] = max(arr[0] + arr[2], arr[1] + arr[2])
if stairs >= 4:
    #이후 층은 점화식을 구하여 계산한다.
    #점화식은 max(dp[i-3]+arr[i-1]+arr[i], dp[i-2]+arr[i])
    for i in range(3, stairs):
        dp[i] = max(dp[i-3]+arr[i-1]+arr[i], dp[i-2]+arr[i])
print(dp[stairs-1])