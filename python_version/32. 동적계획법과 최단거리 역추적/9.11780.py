import sys

#-- inputs --#
input = sys.stdin.readline
INF = sys.maxsize
n = int(input())
m = int(input())
path = [[()]*(n+1) for _ in range(n+1)] # 최단 경로 리스트
costs = [[INF]*(n+1) for _ in range(n+1)] # 최소 비용 리스트
for i in range(1, n+1): # 대각선 즉, 이동이 불가한 a->a는 0으로 비용초기화
    costs[i][i] = 0
for _ in range(m):
    a, b, c = map(int, input().split())
    costs[a][b] = min(costs[a][b], c)
    path[a][b] = (a, b)
    
#-- algo --#
def floyd_warshall():
    for mid in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                cal_cost = costs[i][mid] + costs[mid][j]
                if cal_cost < costs[i][j]:
                    costs[i][j] = cal_cost
                    path[i][j] = path[i][mid] + path[mid][j][1:]
    return

#-- result --#
floyd_warshall()
for i in range(1, n+1):
    line = []
    for j in range(1, n+1):
        if costs[i][j] == INF:
            line.append(0)
        else:
            line.append(costs[i][j])
    print(*line)
for i in range(1, n+1):
    for j in range(1, n+1):
        print(len(path[i][j]), *path[i][j])