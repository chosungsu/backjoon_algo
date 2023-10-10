import sys

input = sys.stdin.readline
N = int(input()) # 컴퓨터의 수
M = int(input()) # 쌍의 수
R = 1 # 시작 정점 초기화
sys.setrecursionlimit(N+10)

#-- 1번 정점부터 시작한다. --#
# 방문한 곳
visited = [False] * (N+1)
#그래프 (정점 집합)
graph = [[]for _ in range(N+1)]

#-- 연결하기 --#
for i in range(M): # 간선의 수 만큼 반복
    u,v = map(int, input().split()) # u,v 입력받기
    graph[u].append(v) # u,v 서로 연결
    graph[v].append(u) # u,v 서로 연결
    
#-- dfs호출시작 --#
count = 0
def dfs(graph, visited, start):
    global count
    
    count += 1
    visited[start] = count
    for i in graph[start]: # 그래프 집합에서
        if visited[i] == False: #방문하지 않은 경우,
            dfs(graph, visited, i)
            
#-- dfs --#
dfs(graph, visited, R)

#-- result --#
print(count-1)