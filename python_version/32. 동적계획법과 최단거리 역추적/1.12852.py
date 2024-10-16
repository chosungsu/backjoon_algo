import sys
input = sys.stdin.readline

N = int(input())
cnt = [0]*(N+1) # 연산 횟수 메모이제이션
path = ["" for _ in range(N+1)] # 최단 경로
path[1] = "1"

for idx in range(2, N+1):
    cnt[idx] = cnt[idx-1] + 1
    prev = idx-1
    if idx % 3 == 0 and cnt[idx//3]+1 < cnt[idx]:
        cnt[idx] = cnt[idx//3] + 1
        prev = idx // 3
    if idx % 2 == 0 and cnt[idx//2]+1 < cnt[idx]:
        cnt[idx] = cnt[idx//2] + 1
        prev = idx // 2
    path[idx] = str(idx) + " " + path[prev] # 이전 값이 뒤로 배치

print(cnt[N])
print(path[N])