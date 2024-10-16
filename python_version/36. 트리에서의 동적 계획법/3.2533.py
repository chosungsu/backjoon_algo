import sys

#-- inputs --#
sys.setrecursionlimit(10 ** 9)
input=sys.stdin.readline
N = int(input())
lines = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    lines[a].append(b)
    lines[b].append(a)
dp = [[0, 0] for _ in range(N + 1)]
visited = [False for _ in range(N + 1)]

#-- algo --#
def dfs(start):
    visited[start] = True
    dp[start][0] = 1
    for i in lines[start]:
        if not visited[i]:
            dfs(i)
            dp[start][0] += min(dp[i][0], dp[i][1])
            dp[start][1] += dp[i][0]

#-- result --#
dfs(1)
print(min(dp[1][0], dp[1][1]))