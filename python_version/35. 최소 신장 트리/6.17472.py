import sys
from collections import deque

#-- inputs --#
input=sys.stdin.readline
N, M = map(int, input().split())
visited = [[False] * M for _ in range(N)]
mapinfo = [list(map(int, input().split())) for _ in range(N)]
distance = ((0,1), (0,-1), (1,0), (-1,0))
edges = set()

#-- algo --#
def isinside(ni, nj):
    return ni < 0 or ni >= N or nj < 0 or nj >= M

def marking(y, x, mark):
    q = deque()
    q.append((y, x))
    mapinfo[y][x] = mark
    visited[y][x] = True
    while q:
        i, j = q.popleft()
        for dy, dx in distance:
            ni, nj = i + dy, j + dx
            if isinside(ni, nj) or not mapinfo[ni][nj] or visited[ni][nj]:   
                continue
            mapinfo[ni][nj] = mark
            visited[ni][nj] = True
            q.append((ni, nj))

def getDist(y, x, now):
    q = deque()
    for idx in range(4):
        q.append((y, x, 0, distance[idx]))
    while q:
        i, j, cnt, nowDir = q.popleft()
        if mapinfo[i][j] != 0 and mapinfo[i][j] != now:
            if cnt > 2:
                edges.add((cnt - 1, now, mapinfo[i][j]))
            continue
        ni, nj = i + nowDir[0], j + nowDir[1]
        if isinside(ni, nj) or mapinfo[ni][nj] == now:   
            continue
        q.append((ni, nj, cnt + 1, nowDir))

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a > b:
        parent[b] = parent[a]
    else:
        parent[a] = parent[b]
          
#-- result --#
mark = 1
for i in range(N):
    for j in range(M):
        if mapinfo[i][j] and not visited[i][j]:
            marking(i, j, mark)
            mark += 1
        
for i in range(N):
    for j in range(M):
        if mapinfo[i][j] != 0: # 땅이 있는 경우
            visited = [[False] * M for _ in range(N)]
            getDist(i, j, mapinfo[i][j])

edge = list(edges)
edge.sort()
parent = [i for i in range(mark)]
result = 0
num = 0
for cost, a, b in edge:
    if find(parent, a) != find(parent, b):
        num += 1
        union(parent, a, b)
        result += cost
        
if result == 0 or  num != mark - 2:
    print(-1)
else:   
    print(result)
            