import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = list(map(int, input().split()))
# 연산을 줄이기 위해 초기 K일 동안의 합은 먼저 생성한다.
dp = [sum(arr[:K])]
# 점화식은 (이전에 구해진 K일 동안의 마지막 합) + ((다음 K일 이후 값) - (이전 K일 전의 값))
for i in range(1, N - K + 1):
    res = dp[-1] + (arr[i + K - 1] - arr[i - 1])
    dp.append(res)
print(max(dp))