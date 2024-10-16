import sys

input = sys.stdin.readline

N, M = map(int, input().split())
arr1 = [list(map(int, input().split())) for _ in range(N)]
M, K = map(int, input().split())
arr2 = [list(map(int, input().split())) for _ in range(M)]

#행렬 곱은 N*M, M*K일 때 N*K 형태로 변환된다.
res = [[0 for _ in range(K)] for _ in range(N)]

for i in range(N):
    for j in range(K):
        a = 0
        for k in range(M):
            a += arr1[i][k] * arr2[k][j]
        res[i][j] = a
for r in res:
    print(*r)