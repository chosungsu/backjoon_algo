import sys

#-- inputs --#
input=sys.stdin.readline
N = int(input())
visited = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * (1 << N - 1) for _ in range(N)]

#-- algo --#
def DFS(i, route):
    if dp[i][route] != 0:
        return dp[i][route]

    if route == (1 << (N - 1)) - 1:
        if visited[i][0]:
            return visited[i][0]
        else:
            return float('inf')
            
    min_dist = float('inf')
    for j in range(1, N):
        if not visited[i][j]:
            continue
        if route & (1 << j - 1):
            continue
        dist = visited[i][j] + DFS(j, route | (1 << (j - 1)))
        if min_dist > dist:
            min_dist = dist
    dp[i][route] = min_dist
    
    return min_dist

#-- result --#
print(DFS(0, 1))  # now: 0번째 도시부터 방문, visited: 0번째 도시 방문 처리