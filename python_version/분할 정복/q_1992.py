import sys

input = sys.stdin.readline

n = int(input())
board = [list(map(int, list(input().strip()))) for _ in range(n)]

def sol(x,y,N):
    check = board[x][y]
    for i in range(x, x + N):
        for j in range(y, y + N):
            if check != board[i][j]: # 0과 1이 공존하는 부분을 -1로 구분
                print("(", end="")
                # 1사분면
                sol(x, y, N // 2)
                # 2사분면
                sol(x, y + N // 2 , N // 2)
                # 3사분면
                sol(x + N // 2, y , N // 2)
                # 4사분면
                sol(x + N // 2, y + N // 2, N // 2)
                print(")", end="")
                return None
    print(1 if check == 1 else 0, end='')
sol(0,0,n)