import sys

input = sys.stdin.readline
N, M = map(int, input().split())
arr = list(map(int, input().split()))
start, end = 1, max(arr)
def binary():
    global start, end
    while start <= end:
        mid = (start + end) // 2
        tree_count = [tree - mid if tree > mid else 0 for tree in arr]
        if sum(tree_count) >= M:
            start = mid + 1
        else:
            end = mid -1
    return end
res = binary()
print(res)
    