# n이 3일 경우
#   3 2 6
# 5 0 0 0
# 3 0 0 0
# 2 0 0 0
# 이 dp의 변화를 아래에 기록
# 일단 5*3, 3*2, 2*6에 해당하는 대각선은 계산횟수 0이다.
#   3 2 6
# 5 0 0 0
# 3 0 0 0
# 2 0 0 0
# 다음으로 살펴볼 부분은 3연산곱이다
# 5*2 부분은 존재하지 않으므로 5*3*2연산이 수행되어야 한다.
# 따라서 5*3 + 3*2 + 5*3*2 = 0 + 0 + 30와 같이 구할 수 있다.
# 3*6은 아래와 같다.
# 3*2 + 2*6 + 3*2*6 = 0 + 0 + 36과 같이 구할 수 있다.
#   3 2 6
# 5 0 30 0
# 3 0 0 36
# 2 0 0 0
# 마지막으로 5*6부분은 min을 사용해야 한다.
# 5*3 + 3*6 + 5*3*6 = 0 + 36 + 90 = 126 또는 5*2 + 2*6 + 5*2*6 = 30 + 0 + 60 = 90의 최소값이므로 90 선택
#   3 2 6
# 5 0 30 90
# 3 0 0 36
# 2 0 0 0

# 이제 본격적인 알고리즘
# 우선 각 dp마다 기본계산을 진행해서 저장한다.
# arr[i][0]*arr[i+1][0]*arr[i+1][1] = 문제에서 N*M*K에 해당
import sys
 
input = sys.stdin.readline
N = int(input())
# arr : [[5, 3], [3, 2], [2, 6]]
arr = [list(map(int, input().split())) for _ in range(N)]
dp = [[0]*N for _ in range(N)]

# 이제 본격적인 알고리즘
# 우선 각 dp마다 기본계산을 진행해서 저장한다.
# arr[start][0] * arr[t][1] * arr[start+term][1] = 문제에서 N*M*K에 해당
# dp[i][j] = i에서 j까지 연산할 때의 최소 연산
for i in range(1, N):
    for j in range(N - i):
        x = j+i
        dp[j][x] = 2**32
        for k in range(j, x):
            dp[j][x] = min(dp[j][x],dp[j][k] + dp[k+1][x]+arr[j][0]*arr[k][1]*arr[x][1])
print(dp[0][N-1])