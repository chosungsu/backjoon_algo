import sys

input = sys.stdin.readline

m = int(input())
f = [0] + list(map(int, input().split())) # f 쿼리 자체를 담는 리스트
dp = [[f[i]] for i in range(m + 1)]

for i in range(1, 19):
    for j in range(1, m + 1):
        dp[j].append(dp[dp[j][i - 1]][i - 1])

q = int(input())
for _ in range(q):
    n, x = map(int, input().split())

    for i in range(18, -1, -1):
        if n >= 1 << i:
            n -= 1 << i
            x = dp[x][i]

    print(x)