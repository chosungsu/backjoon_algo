import sys

#-- inputs --#
input = sys.stdin.readline
sys.setrecursionlimit(10**9)
T = int(input())

#-- algo --#
def DFS(start, cnt):
    visited[start] = 1
    
    for adj_node in graph[start]:
        if visited[adj_node] == 0:
            cnt = DFS(adj_node, cnt+1)
    
    return cnt

#-- result --#
for _ in range(T):
    N, M = map(int, input().split()) # N:국가의 수, M: 비행기의 종류
    graph = [[] for _ in range(N+1)]
    visited = [0]*(N+1)
    
    for _ in range(M): # M만큼 아래에 쌍이 주어지며 방향은 없다.
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    
    print(DFS(1, 0))