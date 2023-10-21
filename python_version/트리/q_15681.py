import sys

#-- inputs --#
sys.setrecursionlimit(10**6)
input=sys.stdin.readline
N,R,Q=map(int,input().split())
graph=[[]for _ in range(N+1)]
visit=[0]*(N+1)
for _ in range(N-1):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

#-- algo --#
def dfs(s):
    global visit
    visit[s]=1
    for i in graph[s]:
        if visit[i]==0: #방문하지 않은 방문 가능 노드가 있다면
            visit[s]+=dfs(i) #방문하며 그 노드의 서브트리 개수를 더해준다
    return visit[s] #내 서브트리 개수를 리턴한다

#-- result --#
dfs(R)
for _ in range(Q):
    get=int(input())
    print(visit[get])