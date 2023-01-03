def dfs():
    if len(res)==m:
        print(' '.join(map(str,res)))
        return
    
    for i in range(1, n+1):
        res.append(i)
        dfs()
        res.pop()
n,m= map(int,input().split())
res = []
dfs()