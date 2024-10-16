import sys

#-- inputs --#
input = sys.stdin.readline
INF = sys.maxsize
N, M = map(int, input().split())
edges = []
for _ in range(M):
    A, B, C = map(int, input().split())
    edges.append((A, B, C))
dist = [INF] * (N + 1)

#-- algo --#
def algo(start):
    dist[start] = 0

    # n번의 라운드를 반복
    for i in range(1, N + 1):
        # 매 라운드마다 모든 간선을 확인
        for j in range(M):
            now, next, cost = edges[j][0], edges[j][1], edges[j][2]
            # 현재 간선을 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if dist[now] != INF and dist[next] > dist[now] + cost:
                dist[next] = dist[now] + cost
                # n번째 라운드에서도 값이 갱신된다면 음수 순환 존재
                if i == N:
                    return True

    return False


#-- result --#
cycle = algo(1)

if cycle:
    print(-1)
else:
    for i in range(2, N + 1):
        # 도달할 수 없는 경우
        if dist[i] == INF:
            print(-1)
        # 도달 가능한 경우
        else:
            print(dist[i])