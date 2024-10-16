N = int(input())
A = list(map(int, input().split()))
# dp1은 downtoup, dp2는 uptodown
dp1 = [1] * N
dp2 = [1] * N

for i in range(1, N):
    for j in range(i):
        if A[i] > A[j]: # 리스트 내의 값이 이전인덱스값보다 큰 경우
            dp1[i] = max(dp1[i], dp1[j] + 1)
for i in range(N - 1, -1, -1):
    for j in range(N - 1, i, -1):
        if A[i] > A[j]:
            dp2[i] = max(dp2[i], dp2[j] + 1)
res = [dp1[k] + dp2[k] - 1 for k in range(N)]
print(max(res))