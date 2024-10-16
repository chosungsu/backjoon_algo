from collections import deque

N, K = map(int, input().split())
arr = deque(range(1, N + 1))
removeperson = []
index = 0

while arr:
    for i in range(K-1):
        arr.append(arr.popleft())
    removeperson.append(arr.popleft())
print("<", end='')
print(', '.join(map(str,removeperson)), end='')
print(">")