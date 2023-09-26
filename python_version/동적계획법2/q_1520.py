import sys, heapq

input = sys.stdin.readline
M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(M)]
# arr와 dp의 형태를 아래에 나타내보자
# 50 45 37 32 30
# 35 50 40 20 25
# 30 30 25 17 28
# 27 24 22 15 10

def bfs():
    queue = [(-arr[0][0], 0, 0)]
    direction = [(1,0), (-1,0), (0,1), (0,-1)]
    dp = [[0] * N for _ in range(M)]
    dp[0][0] = 1 # 초깃값 설정 : 처음 위치는 반드시 거쳐가기 때문
    while queue:
        h, x, y = heapq.heappop(queue)
        for dx, dy in direction:
            # direction x, y를 pop되는 x,y와 더해서 갱신한다.
            nx = dx + x
            ny = dy + y
            if 0 <= nx < M and 0 <= ny < N and arr[nx][ny] < arr[x][y]:
                if dp[nx][ny] == 0:
                    nq = (-arr[nx][ny], nx, ny)
                    heapq.heappush(queue, nq)
                dp[nx][ny] += dp[x][y]
    return dp[M-1][N-1]
print(bfs())