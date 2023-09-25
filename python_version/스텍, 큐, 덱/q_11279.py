import sys, heapq

input = sys.stdin.readline
max_heap = []
N = int(input())
for i in range(N):
    x = int(input())
    # x가 0인 경우
    if x == 0:
        try:
            print(heapq.heappop(max_heap) * (-1))
        except:
            print(0)
    else:
        heapq.heappush(max_heap, x * (-1))