import sys

inpupt = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
arr.sort(key = lambda x: (x[1], x[0]))

end = 0
cnt = 0

for s, e in arr:
    if s >= end: # 시작시간이 마지막 종료 시간보다 크거나 같을 경우
        cnt += 1
        end = e
print(cnt)