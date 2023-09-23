N = int(input())
# 자연수 1의 자리로 구성되기 때문에 0~9까지 10개의 자연수가 해당함.
dp = [[0] * 10 for _ in range(N)]
# 1층 초기화
dp[0] = [0,1,1,1,1,1,1,1,1,1]

for i in range(1, N):
    dp[i][0] = dp[i - 1][1]
    dp[i][9] = dp[i - 1][8]
    for j in range(1, 9):
        dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j + 1]
print(sum(dp[N - 1]) % 1000000000)