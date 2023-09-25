import sys

input = sys.stdin.readline

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

m, z, p = 0, 0, 0

def sol(x, y, N):
    global m,z,p
    check = board[x][y]
    for i in range(x, x + N):
        for j in range(y, y + N):
            if check != board[i][j]:
                for k in range(3):
                    for l in range(3):
                        sol(x + k*N//3, y + l*N//3, N//3)
                return None
    if check == -1:
        m += 1
    elif check == 0:
        z += 1
    else:
        p += 1
sol(0,0,N)
print(m)
print(z)
print(p)