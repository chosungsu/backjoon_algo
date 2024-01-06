import heapq
import sys

# bfs 탐색
def bfs():
    while heap:
        # 제일 쉬운 문제를 팝한다.
        x = heapq.heappop(heap)
        res.append(x) # 문제를 풀었으므로 결과 리스트에 추가

        # 현재 문제를 풀고 풀 수 있는 문제를 확인
        for i in graph[x]:
            visited[i] -= 1 # 간선의 개수를 빼준다. 즉, 선행 문제 개수를 빼준다.

            # 다음 풀 수 있는 문제의 간선 개수가 0이면 문제를 푼다.
            # 더 이상 선행 문제가 없으면 현재 문제를 탐색한다.
            if visited[i] == 0:
                heapq.heappush(heap, i)

input = sys.stdin.readline
n, m = map(int, input().split())
heap = []
graph = [[] for _ in range(n + 1)]  # 그래프
visited = [0] * (n + 1)  # 각 문제의 간선 개수
res = []

# 먼저 푸는 것이 좋은 문제에 대한 정보를 입력 받는다.
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)  # 그래프로 표현
    visited[b] += 1  # 간선의 개수 체크

for i in range(1, n + 1):
    if visited[i] == 0:
        heapq.heappush(heap, i)

bfs()  # bfs 탐색

print(*res, sep=" ")
