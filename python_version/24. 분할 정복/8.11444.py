import sys

input = sys.stdin.readline
n = int(input())
p = 1000000007
mat = [[1,1], [1,0]]

def mul(A, B):
    res = [[0 for _ in range(len(A))] for _ in range(len(A))]
    for x in range(len(A)):
        for y in range(len(A)):
            a = 0
            for k in range(len(A)):
                a += A[x][k] * B[k][y]
            res[x][y] = a % p
    return res
def square(A, N):
    if N == 1:
        for x in range(len(A)):
            for y in range(len(A)):
                A[x][y] %= p
        return A
    
    tmp = square(A, N//2)
    if N % 2 == 0:
        return mul(tmp, tmp)
    else:
        return mul(mul(tmp, tmp), A)    

print(square(mat, n)[0][1])