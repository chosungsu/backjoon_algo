import sys

input = sys.stdin.readline

N, M = map(int, input().split())
#N*N 리스트로 생성
arr = []
for i in range(N):
    a = list(map(int, input().split()))
    arr.append(a)
#누적합 구하기
dp = [[0]*(N+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, N+1):
        dp[i][j] = dp[i][j-1] + dp[i-1][j] - dp[i-1][j-1] + arr[i-1][j-1]
#합을 구하기
for k in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    res = dp[x2][y2] - dp[x2][y1-1] - dp[x1-1][y2] + dp[x1-1][y1-1]
    print(res)