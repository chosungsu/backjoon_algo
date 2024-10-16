import sys

input = sys.stdin.readline
N, S = map(int, input().split())
arr = list(map(int, input().split()))
i, j = 0,0
s = arr[0]
ans = 100001

while True:
    # arr 값이 S보다 같거나 클 경우
    if s >= S:
        s -= arr[i]
        ans = min(ans, j-i+1)
        i += 1
    # arr 값이 S보다 작은 경우
    else:
        j += 1
        # 최대 인덱스에 도달한 경우
        if j == N:
            break
        s += arr[j]
print(0) if ans == 100001 else print(ans)