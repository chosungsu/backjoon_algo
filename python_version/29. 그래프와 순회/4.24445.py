import sys
from collections import deque

input = sys.stdin.readline
N, M, R = map(int, input().split())
sys.setrecursionlimit(N+10)

#--1번 정점부터 시작한다.--#
# 방문한 곳
visited = [False] * (N+1)
#그래프 ( 정점 집합)
graph = [[]for _ in range(N+1)]

#--연결하기--#
for i in range(M): # 간선의 수 만큼 반복
    u,v = map(int, input().split()) # u,v 입력받기
    graph[u].append(v) # u,v 서로 연결
    graph[v].append(u) # u,v 서로 연결

# -- 내림차순 정렬 -- #
for i in range(1,N+1):
    graph[i].sort(reverse=True)
    
# bfs호출시작
count = 0
def bfs(graph, visited, start):
    global count
    
    queue=deque([start])#deque에 적용
    count+=1
    visited[start]=count #첫번째 방문 정점
    
    while queue:
        start=queue.popleft()#큐 맨 앞쪽을 삭제
        
        for i in graph[start]:
            if visited[i]==False:
                count+=1 # n+1 번째 방문 정점
                queue.append(i)
                visited[i]=count

# -- bfs -- #
bfs(graph, visited, R)


for i in range(1, N+1):
    if visited[i]:
        print(visited[i])
    else:
        print(0)