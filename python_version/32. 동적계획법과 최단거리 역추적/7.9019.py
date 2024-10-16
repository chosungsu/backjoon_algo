import sys
from collections import deque

#-- inputs --#
input = sys.stdin.readline
T=int(input())

#-- algo --#
def bfs(a, b):
    q = deque([(a, "")])
    visited = set([a])

    while q:
        x, op = q.popleft()

        if x == b:
            return op

        for nx, no in [(2 * x % 10000, "D"), (x - 1 if x > 0 else 9999, "S"),
                       (x % 1000 * 10 + x // 1000, "L"), (x // 10 + x % 10 * 1000, "R")]:
            if nx not in visited:
                q.append((nx, op + no))
                visited.add(nx)

#-- result --#
for _ in range(T):
    a, b = map(int, input().split())
    print(bfs(a, b))