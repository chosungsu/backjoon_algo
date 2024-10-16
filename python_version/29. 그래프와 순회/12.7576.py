import sys
from collections import deque

#-- inputs --#
input=sys.stdin.readline
M, N = map(int, input().split())
tomatobox = [list(map(int, input().split())) for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

#-- bfs --#
def bfs():
    queue = deque()
    # 익은 토마토인 경우 queue에 적용
    for i in range(N):
        for j in range(M):
            if tomatobox[i][j] == 1:
                queue.append([i, j])
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0 <= nx < N and 0 <= ny < M and tomatobox[nx][ny] == 0:
                tomatobox[nx][ny] = tomatobox[x][y] + 1
                queue.append([nx, ny])

bfs()

res = 0
for tomato in tomatobox:
    for eat in tomato:
        if eat == 0:
            print(-1)
            exit(0)
    res = max(res, max(tomato))
print(res - 1)