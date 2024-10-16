import sys
import math
from collections import deque

input = sys.stdin.readline

N = int(input())
LEN = int(math.log2(N))+1
tree = [[] for _ in range(N + 1)]

for i in range(N - 1):
    a, b, c = map(int, input().split())
    tree[a].append((b,c))
    tree[b].append((a,c))
    
queue = deque([(1, 1)])
depth = [0] * (N + 1)
depth[1] = 1
dp = [[[0,0,0] for _ in range(LEN)] for _ in range(N+1)]

while queue:
    i, d = queue.popleft()
    for j, c in tree[i]:
        if not depth[j]:
            queue.append((j, d + 1))
            depth[j] = d + 1
            dp[j][0] = [i,c,c]

for j in range(1, LEN):
    for i in range(1, N + 1):
        dp[i][j][0] = dp[dp[i][j-1][0]][j-1][0]
        dp[i][j][1] = min(dp[i][j-1][1], dp[dp[i][j-1][0]][j-1][1])
        dp[i][j][2] = max(dp[i][j-1][2], dp[dp[i][j-1][0]][j-1][2])

K = int(input())
for _ in range(K):
    a, b = map(int, input().split())
    max_len = 0
    min_len = float('inf')
        
    if depth[a] > depth[b]:
        a, b = b, a
    for i in range(LEN, -1, -1):
        if depth[b] - depth[a] >= (1<<i):
            min_len = min(dp[b][i][1], min_len)
            max_len = max(dp[b][i][2], max_len)
            b = dp[b][i][0]
    if a == b:
        print(min_len, max_len)
        continue
        
    for i in range(LEN-1, -1, -1):
        if dp[a][i][0] != dp[b][i][0]:
            min_len = min(dp[a][i][1],dp[b][i][1], min_len)
            max_len = max(dp[a][i][2],dp[b][i][2], max_len)
            a = dp[a][i][0]
            b = dp[b][i][0]
    min_len = min(dp[a][0][1],dp[b][0][1], min_len)
    max_len = max(dp[a][0][2],dp[b][0][2], max_len)
    print(min_len, max_len)