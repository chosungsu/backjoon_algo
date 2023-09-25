import sys

input = sys.stdin.readline

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
b, w = 0, 0

def sol(x, y, N):
    global b, w
    color = board[x][y] # 해당 위치의 컬러값(0 : w, 1 : b)
    for i in range(x, x + N):
        for j in range(y, y + N):
            if color != board[i][j]: # 컬러가 다른 컬러임을 인지할 때
                sol(x, y, N //2) # 시작점(x, y) + 절반높이(N//2)
                sol(x, y + N //2, N//2) #  시작점(x, y + N//2) + 절반높이(N//2)
                sol(x + N//2, y, N //2) # 시작점(x + N//2, y) + 절반높이(N//2)
                sol(x + N // 2, y + N //2, N//2) #  시작점(x + N//2, y + N//2) + 절반높이(N//2)
                return
    if color == 0:
        w += 1
    else:
        b += 1
sol(0,0,N)
print(w)
print(b)