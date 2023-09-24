import sys

input = sys.stdin.readline
n,m,k = list(map(int,input().rstrip().split()))
chess=[list(input().strip('\n')) for _ in range(n)]
#board[i][j] : i행 j열까지 자른 이후 바꿔야하는 최소 개수로 설정
#rowcol : 추가할 행과 열(겹치는 부분 제외)
#same : 겹치는 부분
def solution(color):
    row_num=[0]*(n+1)
    col_num=[0]*(m+1)
    res=1e9
    board=[[0]*(m+1) for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, m+1):
            if ((i+j)%2==1 and chess[i-1][j-1]==color) or ((i+j)%2==0 and chess[i-1][j-1]!=color): 
                row_num[i]+=1
                col_num[j]+=1
                board[i][j]=1
            board[i][j]=board[i-1][j-1]+row_num[i]+col_num[j]-board[i][j]
    for i in range(1, n+1):
        row_num[i]+=row_num[i-1]
    for i in range(1, m+1):
        col_num[i]+=col_num[i-1]
    for i in range(k, n+1):
        for j in range(k, m+1):
            temp=board[i][j]-board[i-k][j]-board[i][j-k]+board[i-k][j-k]
            res=min(res, temp)
    return res
print(min(solution('B'), solution('W')))