def dfs(depth):
    if len(res)==m:
        print(' '.join(map(str, res)))
        return
    
    for i in range(depth, n + 1):
        if i not in res:
            res.append(i)
            dfs(i + 1)
            res.pop()
n,m = list(map(int,input().split()))
res = []
dfs(1)