import sys
from collections import deque

N = int(input())
arr = deque()

for _ in range(N):
    n = sys.stdin.readline().strip().split()  # strip()로 개행 문자 제거
    if n[0] == 'push':
        arr.append(n[1])
    elif n[0] == 'pop':
        print(-1) if not arr else print(arr.popleft())
    elif n[0] == 'size':
        print(len(arr))
    elif n[0] == 'empty':
        print(1) if not arr else print(0)
    elif n[0] == 'front':
        print(-1) if not arr else print(arr[0])
    elif n[0] == 'back':
        print(-1) if not arr else print(arr[-1])
