import sys

input = sys.stdin.readline
N = int(input())
K = int(input())
start, end = 1, K
def binary():
    global start, end
    while start <= end:
        mid = (start + end) // 2
        num_count = [min(mid//arr, N) for arr in range(1, N + 1)]
        if sum(num_count) >= K:
            end = mid -1
        else:
            start = mid + 1
    return start
res = binary()
print(res)
    