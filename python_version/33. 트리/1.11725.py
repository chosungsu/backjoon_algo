import sys

#-- inputs --#
sys.setrecursionlimit(10**6)
N = int(input())
tree = [[] for _ in range(N + 1)]
parent = [None for _ in range(N + 1)]
# 주어진 노드로 트리 값 할당(양방향)
for _ in range(N - 1):
    node_a, node_b = map(int, input().split())
    tree[node_a].append(node_b)
    tree[node_b].append(node_a)
    
#-- algo --#
def DFS(graph, v, visited):
    for i in graph[v]:
        # 만약 방문하지 않았을 경우 방문할 정점의 값을 할당하고 재귀함수 호출
        if not visited[i]:
            visited[i] = v
            DFS(graph, i, visited)



#-- result --#
DFS(tree, 1, parent)
# 각 노드의 부모 노드 번호를 루트인 1번을 제외하고 2번부터 순서대로 출력
for i in range(2, N + 1):
    print(parent[i])