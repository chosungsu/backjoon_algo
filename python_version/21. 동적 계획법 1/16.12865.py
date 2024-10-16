N, K = map(int, input().split())
arr = [[0, 0] if i == 0 else list(map(int, input().split())) for i in range(N + 1)]
dp = [[0] * (K+1) for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, K + 1):
        w = arr[i][0]
        v = arr[i][1]
        if w > j: # 무게 초과
            dp[i][j] = dp[i - 1][j]
        else: # 무게 미초과
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w] + v)
print(dp[N][K])