import sys
from collections import deque

N = int(input())
list_a = list(map(int, sys.stdin.readline().split()))  # 0 1 1 0 (0 = queue, 1 = stack)
list_b = list(map(int, sys.stdin.readline().split()))  # 1 2 3 4
M= int(input())
list_c = list(map(int, sys.stdin.readline().split())) # 2 4 7

# stack : 후입선출, queue : 선입선출
# 따라서 후입선출인 stack은 문제에서 pop을 제시 할 명분이 없다고 생각함.
res = deque()
for i in range(N):
    # queue만 진행함. 선입선출로 왼쪽으로 추가하도록 함.
    if list_a[i] == 0:
        res.appendleft(list_b[i])
for j in range(M):
    res.append(list_c[j])
    print(res.popleft(), end=' ')