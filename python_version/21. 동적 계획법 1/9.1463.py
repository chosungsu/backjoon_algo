n = int(input())
dp = [0] * (n+1)

#n이 1인 경우 : 1->1의 연산이 0회로 고민x
#n이 2인 경우 : 2->1의 연산이 1회(1 빼기)로 연산을 2부터 시작하게 함.
for i in range(2, n+1):
    dp[i] = dp[i-1] + 1
    if i % 3 == 0: # 3으로 나누어 떨어지는 수일 경우
        dp[i] = min(dp[i], dp[i // 3] + 1)
    if i % 2 == 0: # 2로 나누어 떨어지는 수일 경우
        dp[i] = min(dp[i], dp[i // 2] + 1)
print(dp[n])
