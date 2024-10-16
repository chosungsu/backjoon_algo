import sys

input = sys.stdin.readline
N, M = map(int, input().split())
arr = list(map(int, input().split()))
# 누적 합을 계산
for i in range(1, N):
    arr[i] += arr[i-1]
arr = [0] + arr
#5 4 3 2 1
#0 5 9 12 14 15
for i in range(M):
    i, j = map(int, input().split())
    print(arr[j] - arr[i-1])