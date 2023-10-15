import sys

#-- inputs --#
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
N=int(input())
W=int(input())
case = []
for _ in range(W):
    x,y = map(int,input().split())
    case.append((x,y))
case1=[(1,1)]+case # 경찰차1
case2=[(N,N)]+case # 경찰차2\
dp = [[0]*(W+1) for _ in range(W+1)]

#-- algo --#
def DFS(p1,p2):
    global N, W, dp
    if p1==W or p2==W:
        return 0
    if dp[p1][p2]!=0:
        return dp[p1][p2]
    x=case1[p1][0]
    y=case1[p1][1]
    a=case2[p2][0]
    b=case2[p2][1]
    next=max(p1,p2)+1
    l1=abs(case[next-1][0]-x)+abs(case[next-1][1]-y)
    l2=abs(case[next-1][0]-a)+abs(case[next-1][1]-b)
    dp[p1][p2] = min(l1+DFS(next,p2),l2+DFS(p1,next))
    return dp[p1][p2]

def PATH(p1,p2):
    global N, W, dp
    if p1==W or p2==W:
        return
    x=case1[p1][0]
    y=case1[p1][1]
    a=case2[p2][0]
    b=case2[p2][1]
    next=max(p1,p2)+1
    l1=abs(case[next-1][0]-x)+abs(case[next-1][1]-y)
    l2=abs(case[next-1][0]-a)+abs(case[next-1][1]-b)
    if l1+dp[next][p2] < l2+dp[p1][next]: # 경찰차1이 가까운 경우
        print(1)
        PATH(next,p2)
    else: # 경찰차2가 가까운 경우
        print(2)
        PATH(p1,next)

#-- result --#
p1,p2 = 0,0
print(DFS(p1,p2))
PATH(p1,p2)