import sys, heapq

input = sys.stdin.readline
abs_heap = []
N = int(input())

# 정렬 시에 절댓값을 시킨 값을 push하면서 절댓값 순 정렬이 필요하다.
# 출력 시에 동일 절댓값 중 가장 작은 수를 출력하는 것이 필요하다.
for i in range(N):
    x = int(input())
    if x == 0:
        try:
            print(heapq.heappop(abs_heap)[1])
        except:
            print(0)
    else:
        heapq.heappush(abs_heap, (abs(x), x))