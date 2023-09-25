import sys

input = sys.stdin.readline

N, B = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

def mul(A, B):
    res = [[0 for _ in range(len(A))] for _ in range(len(A))]
    for x in range(len(A)):
        for y in range(len(A)):
            a = 0
            for k in range(len(A)):
                a += A[x][k] * B[k][y]
            res[x][y] = a % 1000
    return res
def sol(N, B, arr):
    if B == 1:
        for x in range(N):
            for y in range(N):
                arr[x][y] %= 1000
        return arr
    else:
        tmp = sol(N, B//2, arr)
        if B % 2 == 0:
            return mul(tmp, tmp)
        else:
            return mul(mul(tmp, tmp), arr)

ans = sol(N, B, arr)
for r in ans:
    print(*r)