N = int(input())
lists = []
dp = [1]*N

for i in range(N):
    a, b = map(int, input().split())
    lists.append([a, b])

# key 순서(A 우선)으로 정렬
lists.sort()

# 겹치는 부분을 찾는 방법
# 정렬된 리스트에서 A 기준 B값이 이전 인덱스가 더 클 경우 겹침으로 판단 가능
for j in range(1, N):
    for k in range(0, j):
        if lists[k][1] < lists[j][1]:
            dp[j] = max(dp[j], dp[k] + 1)
# 최소 갯수는 전체 개수에서 max를 소거하여 구한다.
print(N - max(dp))