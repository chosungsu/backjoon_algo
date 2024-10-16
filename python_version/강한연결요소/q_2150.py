import sys
from collections import defaultdict, deque
sys.setrecursionlimit(10**6)
 
def dfs(cur):
    visited.add(cur)
 
    for next in forwardGraph[cur]:
        if next not in visited:
            dfs(next)
    stack.append(cur)
 
def reverseDfs(cur, scc):
    visited.add(cur)
    scc.append(cur)
 
    for next in reverseGraph[cur]:
        if next not in visited:
            scc = reverseDfs(next, scc)
    return scc
 
def kosaraju():
    global visited
    answer = []
    # 정방향 그래프를 돌면서 dfs 실행
    for i in range(1, V+1):
        if i not in visited:
            dfs(i)
 
    visited = set()
    while stack:
        scc = []
        cur = stack.pop()
 
        if cur in visited:
            continue
 
        answer.append(sorted(reverseDfs(cur, scc)))
    return answer
 
V, E = map(int, sys.stdin.readline().split())
forwardGraph = defaultdict(list)
reverseGraph = defaultdict(list)
 
for _ in range(E):
    A, B = map(int, sys.stdin.readline().split())
    forwardGraph[A].append(B)
    reverseGraph[B].append(A)
 
stack = []
visited = set()
answer = kosaraju()
 
print(len(answer))
for line in sorted(answer):
    print(*line, sep = ' ', end = ' -1\n')