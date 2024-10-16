import sys

#-- inputs --#
input = sys.stdin.readline
A = input()
B = input()
NA=len(A)
NB=len(B)
dp=[[0 for _ in range(NB)] for _ in range(NA)]
res=[]
x=NA-1
y=NB-1

#-- algo --#
for i in range(1, NA):
    for j in range(1, NB):
        if A[i-1] == B[j-1]: # 각 문자가 동일한 경우
            dp[i][j] = dp[i-1][j-1] + 1 # dp에 추가
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
while x > 0 and y > 0:
    if dp[x][y-1] == dp[x][y]:
        y -= 1
    elif dp[x-1][y] == dp[x][y]:
        x -= 1
    else:
        res.append(A[x-1])
        x -= 1
        y -= 1

#-- result --#
print(dp[NA-1][NB-1])
for c in res[::-1]:
    print(c, end='')
print()