import sys

N, M = map(int, input().split())
arr = dict()

for i in range(N):
    strs = sys.stdin.readline().rstrip()
    if len(strs) >= M:
        if strs in arr: # 단어가 있는 경우
            arr[strs] += 1
        else: # 단어가 없는 경우
            arr[strs] = 1
# 개수, 길이는 내림차순, 단어는 사전순 정렬
ans = sorted(arr.items(), key=lambda x:(-x[1], -len(x[0]), x[0]))

for a in ans:
    print(a[0])