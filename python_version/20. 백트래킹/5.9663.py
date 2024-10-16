import sys

input = sys.stdin.readline
N = int(input())
res = 0
arr = [[0]*N for _ in range(N)]

# 열에 퀸이 놓였는지 표시
col = [0] * N
# 대각선 표시를 위한 배열
dial1 = [0] * (N*2-1) # r + c에 대한 대각선 표기
dial2 = [0] * (N*2-1) # r - c + N-1

def dfs(depth):
    global res
    
    if depth == N:
        res += 1
    else:
        for i in range(N):
            if not col[i] and not dial1[depth+i] and not dial2[depth - i + N-1]:
                arr[depth][i] = 1
                col[i] = 1
                dial1[depth + i] = 1
                dial2[depth - i + N-1] =1

                dfs(depth + 1)

                arr[depth][i] = 0
                col[i] = 0
                dial1[depth + i] = 0
                dial2[depth - i + N - 1] = 0

dfs(0)
print(res)