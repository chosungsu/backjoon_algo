import sys
from collections import deque

input = sys.stdin.readline
N, M, V = map(int, input().split())
sys.setrecursionlimit(N+10)

#그래프 (정점 집합)
graph = [[]for _ in range(N+1)]

#--연결하기--#
for i in range(M): # 간선의 수 만큼 반복
    u,v = map(int, input().split()) # u,v 입력받기
    graph[u].append(v) # u,v 서로 연결
    graph[v].append(u) # u,v 서로 연결

# -- 오름차순 정렬 -- #
for i in range(1,N+1):
    graph[i].sort()
    
#-- dfs --#
# 방문한 곳
visited_dfs = [False] * (N+1)

count_dfs = 0
def dfs(graph, visited, start):
    global count_dfs
    
    count_dfs += 1
    visited[start] = count_dfs
    print(start, end=" ")
    for i in graph[start]: # 그래프 집합에서
        if visited[i] == False: #방문하지 않은 경우,
            dfs(graph, visited, i)
            

#-- bfs --#
# 방문한 곳
visited_bfs = [False] * (N+1)
    
count_bfs = 0
def bfs(graph, visited, start):
    global count_bfs
    
    queue=deque([start])#deque에 적용
    count_bfs+=1
    visited[start]=count_bfs #첫번째 방문 정점
    
    while queue:
        start=queue.popleft()#큐 맨 앞쪽을 삭제
        print(start, end=" ")
        
        for i in graph[start]:
            if visited[i]==False:
                count_bfs+=1 # n+1 번째 방문 정점
                queue.append(i)
                visited[i]=count_bfs
                
#-- result --#
dfs(graph, visited_dfs, V)
print()
bfs(graph, visited_bfs, V)