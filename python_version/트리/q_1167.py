import sys
from collections import deque

#-- inputs --#
input=sys.stdin.readline
sys.setrecursionlimit(10**6)
V = int(input())
# 각 노드의 연결된 정보를 트리로 표현
graph = [[] for _ in range(V + 1)]
for _ in range(V):
    w = list(map(int, input().split()))
    # 두개씩 짝이 지어져 있음(정점번호, 거리정수)
    for j in range(1, len(w) - 2, 2):
        graph[w[0]].append([w[j], w[j + 1]])
    
#-- algo --#
def bfs(start):
    que = deque()
    que.append(start)
    visited = [-1] * (V + 1) # 탐색 여부, 간선의 거리
    visited[start] = 0
    _max = [0, 0]

    while que:
        t = que.popleft()
        for e, w in graph[t]:
            if visited[e] == -1:
                visited[e] = visited[t] + w
                que.append(e)
                if _max[0] < visited[e]:
                    _max = visited[e], e

    return _max

#-- result --#
dis, node = bfs(1)
dis, node = bfs(node)
print(dis)