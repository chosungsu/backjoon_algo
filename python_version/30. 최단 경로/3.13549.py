import sys
from collections import deque

#-- input --#
input=sys.stdin.readline
N, K = map(int, input().split())  # n: 수빈이가 있는 위치, k: 동생이 있는 위치
q = deque()
q.append(N) 
visited = [-1 for _ in range(100001)]
visited[N] = 0

while q:
    now = q.popleft()
    if now == K:
        print(visited[now])
        break
    if 0 <= now-1 < 100001 and visited[now-1] == -1:
        visited[now-1] = visited[now] + 1
        q.append(now-1)
    if 0 < now*2 < 100001 and visited[now*2] == -1:
        visited[now*2] = visited[now]
        q.appendleft(now*2)  # 2*s 가 다른 연산보다 더 높은 우선순위를 가지기 위함
    if 0 <= now+1 < 100001 and visited[now+1] == -1:
        visited[now+1] = visited[now] + 1
        q.append(now+1)