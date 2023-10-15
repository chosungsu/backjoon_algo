import sys
from collections import deque

#-- inputs --#
input=sys.stdin.readline
N, K = map(int,input().split())
dist = [-1] * (100001)
prev = [-1] * (100001)

#-- algo --#
def bfs(n):
    global K
    q = deque([n])
    dist[n] = 0

    while q:
        n = q.popleft()

        if n == K:
            return dist[K]

        for nx in (n - 1, n + 1, n * 2):
            if 0 <= nx < 100001 and dist[nx] == -1:
                q.append(nx)
                dist[nx] = dist[n] + 1
                prev[nx] = n


def path(k):
    a = []
    temp = k

    for _ in range(dist[k] + 1):
        a.append(temp)
        temp = prev[temp]

    return a[::-1]

#-- result --#
print(bfs(N))
print(*path(K))