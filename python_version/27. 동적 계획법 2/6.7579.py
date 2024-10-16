import sys

input = sys.stdin.readline
N, M = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

tc = sum(arr2)
dp = [[0 for _ in range(tc + 1)] for _ in range(N + 1)]
result = sys.maxsize

for i in range(N):
    memory = arr1[i]
    cost = arr2[i]
    
    for j in range(tc):
        # cost가 비용 j를 넘어가면 종료를 할 수 없어 이전값을 그대로 가져온다.
        if j < cost:
            dp[i][j] = dp[i-1][j]
        # cost가 비용 j를 넘어가지 않으면 종료시키지 않는 경우와 종료시킨 경우의 최대값으로 반영
        else:
            dp[i][j] = max(dp[i-1][j], arr1[i] + dp[i-1][j-cost])
        
        if dp[i][j] >= M:
            result = min(result, j)
if M==0:
    print(0)
elif N==1:
    print(arr2[0])
elif result == sys.maxsize:
    print(N*M)
else:
    print(result)