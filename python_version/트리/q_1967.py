import sys

#-- inputs --#
input = sys.stdin.readline
sys.setrecursionlimit(10**5)
N = int(input())
graph = [[] for _ in range(N + 1)]
# 트리 구현
for _ in range(N - 1):
    a, b, c = map(int, input().split()) # a:부모노드번호, b:자식노드, c:간선의 가중치
    graph[a].append([b, c])
    graph[b].append([a, c])

#-- algo --#
def dfs(x, w):
    for i in graph[x]:
        a, b = i
        if visited[a] == -1:
            visited[a] = w + b
            dfs(a, w + b)


#-- result --#
# 1번 노드에서 가장 먼 곳을 찾는다.
visited = [-1] * (N + 1)
visited[1] = 0
dfs(1, 0)

# 위에서 찾은 노드에 대한 가장 먼 노드를 찾는다.
start = visited.index(max(visited))
visited = [-1] * (N + 1)
visited[start] = 0
dfs(start, 0)

print(max(visited))