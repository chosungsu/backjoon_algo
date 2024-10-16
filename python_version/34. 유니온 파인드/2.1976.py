#-- inputs --#
n = int(input()) # 도시 수
m = int(input()) # 계획한 도시 수
parents = list(range(n))
graph = [list(map(int, input().split())) for _ in range(n)]
plan = list(map(int, input().split())) # 마지막 줄에는 여행 계획을 입력

#-- algo --#
def find(a):
    if parents[a] != a:
        parents[a] = find(parents[a])
    return parents[a]
def union(a, b):
    a = find(a)
    b = find(b)
    if a > b:
        parents[a] = b
    else:
        parents[b] = a

#-- result --#
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            union(i, j)
ans = "YES"
for i in range(1, m):
    if parents[plan[i] - 1] != parents[plan[0] - 1]:
        ans = "NO"
        break
print(ans)