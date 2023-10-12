import sys
from collections import deque

input=sys.stdin.readline
T = int(input()) # 테스트 케이스 개수(반복문에 사용)

for _ in range(T):
    NL = int(input()) # 체스판의 한변 길이(가로*세로)
    now = list(map(int, input().split())) # 현재 위치
    move = list(map(int, input().split())) # 이동할 위치

    chess = [[0]*NL for _ in range(NL)] # 체스판을 matrix화
    visited = [[False]*NL for _ in range(NL)] # 방문여부
    
    # 시계방향 기준으로 이동할 수 있는 x,y좌표 리스트화
    dx = [-2, -1, 1, 2, 2, 1, -1, -2]
    dy = [1, 2, 2, 1, -1, -2, -2, -1]


    def bfs():
        queue = deque()
        queue.append(now)
        visited[now[0]][now[1]]

        while queue:
            x, y = queue.popleft()

            if x == move[0] and y == move[1] :
                return 0

            for i in range(8):
                nx = x+dx[i]
                ny = y+dy[i]

                if nx <0 or nx>=NL or ny<0 or ny>=NL: # 무시해야 하는 경우
                    continue

                if nx == move[0] and ny == move[1]:
                    visited[nx][ny] = True
                    return chess[x][y]+1

                if visited[nx][ny] == False:
                    queue.append([nx,ny])
                    visited[nx][ny] = True
                    chess[nx][ny] = chess[x][y] + 1    
    
    print(bfs())