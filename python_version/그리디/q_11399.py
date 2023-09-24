import sys

input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
arr.sort()
cnt = 0

for a in range(1, N + 1):
    cnt += sum(arr[0:a])
print(cnt)