import sys
from collections import deque

#-- inputs --#
input=sys.stdin.readline
M, N, H = map(int, input().split())
tomatobox = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
visited = [[[0]*M for _ in range(N)] for _ in range(H)]
dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

#-- bfs --#
def bfs():
    queue = deque()
    # 익은 토마토인 경우 queue에 적용
    for i in range(H):
        for j in range(N):
            for k in range(M):
                if tomatobox[i][j][k] == 1 and visited[i][j][k] == 0:
                    queue.append((i, j, k))
                    visited[i][j][k] = 1
    while queue:
        x, y, z = queue.popleft()
        for i in range(6):
            nx = dx[i] + x
            ny = dy[i] + y
            nz = dz[i] + z
            if nx < 0 or nx >= H or ny < 0 or ny >= N or nz < 0 or nz >= M:
                continue
            if tomatobox[nx][ny][nz] == 0 and visited[nx][ny][nz] == 0:
                queue.append((nx, ny, nz))
                tomatobox[nx][ny][nz] = tomatobox[x][y][z] + 1
                visited[nx][ny][nz] = 1

bfs()

res = 0
for tomato in tomatobox:
    for eat in tomato:
        for eats in eat:
            if eats == 0:
                print(-1)
                exit(0)
        res = max(res, max(eat))
print(res - 1)