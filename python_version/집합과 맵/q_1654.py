import sys

input = sys.stdin.readline
K, N = map(int, input().split())
lan = [int(input()) for _ in range(K)]
# 0, max(lan)-1로 설정하지 않은 이유는 0이 나오면 안되기 때문이다.
start, end = 1, max(lan)

def binary_search():
    global start, end
    while start <= end:
        mid = (start + end) // 2
        cable_count = [(i // mid) for i in lan]
        if sum(cable_count) >= N:
            start = mid + 1
        else:
            end = mid -1
    return end
res = binary_search()
print(res)