import sys

#-- inputs --#
input = sys.stdin.readline
n, m = map(int, input().split())
case = 1 # 케이스 정보가 주어지지 않아 초기화


#-- algo --#
# start 노드부터 시작하여 DFS를 끝까지 돌고
# 사이클 존재 여부를 리턴하는 함수
def findCycle(start):
    for adj_node in graph[start]:
        # 인접 노드가 자신의 부모 노드인 경우 패스
        if parent[start] == adj_node:
            continue
        
        # 인접 노드가 부모 노드가 아닌데 방문 이력이
        # 있다는 것은 곧 사이클을 의미함
        if visited[adj_node]:
            return True
        
        parent[adj_node] = start
        visited[adj_node] = 1
        # 인접 노드를 루트 노드로 하는 서브트리에
        # 사이클이 존재하면 곧 전체 트리에 사이클이
        # 존재하는 것과 같음
        if findCycle(adj_node):
            return True
    
    return False


#-- result --#
while n != 0 or m != 0:
    graph = [[] for _ in range(n+1)]
    parent = [-1]*(n+1)
    visited = [0]*(n+1)
    count = 0
    
    # 양방향 매핑
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    
    # visited가 0인 모든 노드를 돌면서
    # 가능한 모든 연결 요소(연결 그래프)를 순회함
    for node in range(1, n+1):
        if visited[node] == 0:
            parent[node] = node
            visited[node] = 1
            if not findCycle(node):
                count += 1
    
    if count == 0:
        print(f'Case {case}: No trees.')
    elif count == 1:
        print(f'Case {case}: There is one tree.')
    else:
        print(f'Case {case}: A forest of {count} trees.')
    
    case += 1
    n, m = map(int, input().split()) 