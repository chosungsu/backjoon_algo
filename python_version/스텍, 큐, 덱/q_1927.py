import sys, heapq

input = sys.stdin.readline
min_heap = []
N = int(input())
for i in range(N):
    x = int(input())
    if x == 0:
        try:
            print(heapq.heappop(min_heap))
        except:
            print(0)
    else:
        heapq.heappush(min_heap, x)
        