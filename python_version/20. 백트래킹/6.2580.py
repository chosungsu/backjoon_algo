import sys
input = sys.stdin.readline
board = [list(map(int,input().split())) for _ in range(9)]
blank_arr=[]
row = [[0]*10 for _ in range(9)]
col = [[0]*10 for _ in range(9)]
rec = [[0]*10 for _ in range(9)]

for i in range(9):
    for j in range(9):
        if board[i][j]:
            row[i][board[i][j]]=1
            col[j][board[i][j]]=1
            rec[(i//3)*3+(j//3)][board[i][j]]=1
        else:
            blank_arr.append((i,j))

def dfs(depth):
    if depth==len(blank_arr):
        for i in range(9):
            print(*board[i])
        sys.exit()

    x,y=blank_arr[depth]
    for i in range(1,10):
        if not row[x][i] and not col[y][i] and not rec[(x//3)*3+(y//3)][i]:
            board[x][y]=i
            row[x][i]=1
            col[y][i]=1
            rec[(x//3)*3+(y//3)][i]=1
            dfs(depth+1)
            row[x][i]=0
            col[y][i]=0
            rec[(x//3)*3+(y//3)][i]=0

dfs(0)