N = int(input())
A = list(map(int, input().split()))
dp = [1] * N
for i in range(1, N):
    for j in range(i):
        if A[i] > A[j]: # 리스트 내의 값이 이전인덱스값보다 큰 경우
            dp[i] = max(dp[i], dp[j] + 1)
            
print(max(dp))