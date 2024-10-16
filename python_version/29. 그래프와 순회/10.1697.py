import sys
from collections import deque

#-- inputs --#
input = sys.stdin.readline
MAX = 100001
N, K = map(int, input().split())
array = [0] * MAX

#-- bfs --#
def bfs(v):
    q = deque([v]) # deque에 적합시킴
    while q:
        v = q.popleft()
        if v == K: # 수빈이와 동생이 만나는 경우
            return array[v]
        for next_v in (v-1, v+1, 2*v): # 조건(뒤로 이동, 앞으로 이동, 순간이동)
            if 0 <= next_v < MAX and not array[next_v]:
                array[next_v] = array[v] + 1
                q.append(next_v)

#-- result --#
print(bfs(N))