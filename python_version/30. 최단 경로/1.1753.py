import sys
import heapq

#-- inputs --#
input=sys.stdin.readline
V,E=map(int, input().split())
start=int(input())
graph = [[] for _ in range(V+1)]
node=[sys.maxsize]*(V+1)
for _ in range(E):
    u,v,w=map(int, input().split())
    #방향성이 있어서 u에만 입력
    graph[u].append((v,w))
    
#-- 다익스트라 알고리즘 --#
def algo(start):
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
            cost = dist + i[1]
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < node[i[0]]:
                node[i[0]] = cost
                heapq.heappush(heap, (cost, i[0]))
            
#-- result --#                
algo(start)
for i in node[1:]:
    if i != sys.maxsize:
        print(i)
    else:
        print("INF")