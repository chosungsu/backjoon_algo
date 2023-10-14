import sys
import heapq

#-- inputs --#
input=sys.stdin.readline
start=1
N,E=map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(E):
    a,b,c=map(int, input().split())
    #방향성이 없어 a,b에 모두 입력
    graph[a].append((b,c))
    graph[b].append((a,c))
v1,v2=map(int, input().split()) # 반드시 지나야 하는 정점
    
#-- 다익스트라 알고리즘 --#
def algo(start,end):
    node=[sys.maxsize]*(N+1)
    heap = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여, 큐에 삽입
    heapq.heappush(heap, (0, start))
    node[start] = 0

    while heap:
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(heap)
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if node[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost = node[now] + i[1]
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < node[i[0]]:
                node[i[0]] = cost
                heapq.heappush(heap, (cost, i[0]))
    return node[end]
            
#-- result --#
v1_path = algo(start, v1) + algo(v1, v2) + algo(v2, N)
v2_path = algo(start, v2) + algo(v2, v1) + algo(v1, N)

result = min(v1_path, v2_path)
print(result if result < sys.maxsize else -1)