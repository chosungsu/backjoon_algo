import sys
import heapq

#-- inputs --#
input = sys.stdin.readline
n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    startnum, endnum, cost = map(int, input().split())
    graph[startnum].append((endnum, cost))
start, end = map(int, input().split())

# 가장 가까운 노드를 기록
nearnest = [start] * (n + 1)
distance = [1e9] * (n + 1)

q = [(0, start)]
while q:
    dist, now = heapq.heappop(q)
    if dist > distance[now]:
        continue
    
    for next, nextDist in graph[now]:
        cost = nextDist + dist
        if cost < distance[next]:
            distance[next], nearnest[next] = cost, now
            heapq.heappush(q, (cost, next))
    
res = []
tmp = end
while tmp != start:
    res.append(str(tmp))
    tmp = nearnest[tmp]

res.append(str(start))
res.reverse()

print(distance[end])
print(len(res))
print(" ".join(res))