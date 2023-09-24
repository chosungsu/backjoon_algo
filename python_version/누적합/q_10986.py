import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))
sums = 0
# M으로 나눈 나머지에 해당하는 값을 카운트하는 리스트 생성
# 나머지 < M이므로 길이는 M만큼 생성
dp = [0] * M
# 누적 합을 계산
for i in range(N):
    sums += arr[i]
    dp[sums % M] += 1
# 결과 도출
res = dp[0]
for j in dp:
    res += j * (j - 1) // 2
print(res)