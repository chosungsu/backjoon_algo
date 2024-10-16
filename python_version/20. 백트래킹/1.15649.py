def dfs(depth):
    if depth == m :
        print(' '.join(map(str, res)))
        return
    for i in range(1, n + 1) :
        if visited[i] != 1 :
            visited[i] = 1
            res.append(i)
            dfs(depth + 1)
            visited[i] = 0
            res.pop()
n, m = map(int, input().split())
res = []
visited = [0] * (n + 1)
dfs(0)