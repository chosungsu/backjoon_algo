import sys
from collections import deque

#-- inputs --#
input=sys.stdin.readline
N, M = map(int, input().split())
gameboard = [i for i in range(101)]
for _ in range(N + M):
    a, b = map(int, input().split())
    gameboard[a] = b
visited = [0] * 101
start=1

#-- bfs --#
def bfs(start):
    queue = deque([start])
    visited[start] = 1

    while queue:
        target = queue.popleft()
        # 주사위 눈만큼 반복한다.
        for i in range(1, 7):
            dice = target + i
            # 100칸이 넘어가면 무시
            if dice > 100:
                continue
            move = gameboard[dice]
            if visited[move] == 0:
                queue.append(move)
                visited[move] = visited[target] + 1
                # 100번째 칸까지 탐색했다면 리턴
                if move == 100:
                    return

#-- result --#
bfs(start)
print(visited[100] - 1)