#n=1 -> '1'
#n=2 -> '00' , '11'
#n=3 -> {'00' * x + '1' * y} = {'001', '100', '111'}
#n=4 -> {'0000', '0011', '1001', '1100', '1111'}

N = int(input())
dp = [0] * (N+1)
if N >= 1:
    dp[1] = 1
if N >= 2:
    dp[2] = 2
for i in range(3, N+1):
    dp[i] = (dp[i-1] + dp[i-2]) % 15746
print(dp[N])