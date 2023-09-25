import sys

input = sys.stdin.readline

A, B, C = map(int, input().split())

def sol(A, B, C):
    if B == 1:
        return A%C
    else:
        tmp = sol(A, B // 2, C)
        if B % 2 == 0: # 분할이 가능한 경우
            return tmp * tmp % C
        else:
            return tmp * tmp * A % C

print(sol(A, B, C))