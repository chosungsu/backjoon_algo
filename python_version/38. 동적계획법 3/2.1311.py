import sys

#-- inputs --#
input = sys.stdin.readline
INF = 10**6
N = int(input()) # N이 작으면 비트마스킹 항상 염두
tasks = [list(map(int, input().split())) for _ in range(N)]
visited = [[INF]*(1<<N) for i in range(N+1)]

#-- algo --#
def DFS(n,bit):
    if n == N:
        visited[n][bit] = 0
        return
    for i in range(N):
        if bit&(1<<i):
            continue
        if visited[n+1][bit|(1<<i)] == INF:
            DFS(n+1,bit|(1<<i))
        visited[n][bit] = min(visited[n][bit],visited[n+1][bit|(1<<i)]+tasks[i][n])  

#-- result --#
DFS(0,0)
print(visited[0][0])