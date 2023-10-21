import sys

#-- inputs --#
input=sys.stdin.readline
N = int(input())
W = [0]+ list(map(int, input().split()))
tree = [[] for _ in range(N+1)]
for _ in range(N-1):
    u,v = map(int,input().split())
    tree[u].append(v)
    tree[v].append(u)
    
#-- algo --#
dp=[ [0,0] for _ in range(N+1) ]
visited = [0 for _ in range(N+1)]
def dynamic(node):
    if visited[node] == 1:    
        return max(dp[node][0], dp[node][1])

    visited[node]=1
    dp[node][1]=W[node]
    
    for child in tree[node]:
        if visited[child]==0:
            dynamic(child)
            
            dp[node][0] += max(dp[child][1], dp[child][0])
            
            dp[node][1] += dp[child][0] 
    
    return max(dp[node][0], dp[node][1])

result = dynamic(1)
check = [0 for _ in range(N+1)]
visited = [0 for _ in range(N+1)]
def findPath(node,ps):
    if visited[node]==1:
        return    
    visited[node]=1
    
    if ps==1:
        check[node]=0
        for child in tree[node]:
            if visited[child]==0:
                findPath(child, 0)
    else:
        if dp[node][0]> dp[node][1]:
            check[node]=0

            for child in tree[node]:
                if visited[child]==0:
                    findPath(child,0)    
            
        else:
            check[node]=1

            for child in tree[node]:
                if visited[child]==0:
                    findPath(child,1)    

#-- result --#
findPath(1, 0)
print(result)
for i in range(N+1):
    if check[i]==1:
        print(i, end=' ')