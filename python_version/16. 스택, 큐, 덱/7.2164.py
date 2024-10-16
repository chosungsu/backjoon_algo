from collections import deque

arr = deque(range(1, int(input()) + 1))

# arr이 비어질 때까지 반복됨
while True:
    if len(arr) == 1:
        break
    else:
        arr.popleft()
        arr.rotate(-1)
print(arr[0])