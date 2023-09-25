import sys

input = sys.stdin.readline
N, C = map(int, input().split())
arr = [int(input()) for _ in range(N)]
arr.sort()
start, end = 1, max(arr) - min(arr)
res = 0
def binary():
    global start, end, res
    
    while start <= end:
        # 설치 가능 갯수는 1로 초기화
        cnt = 1
        # 비교군을 첫번째 거리값으로 초기화
        currenthouse = arr[0]
        mid = (start + end) // 2
        for i in range(1, N):
            # mid를 더한 직전의 거리값이 현재 거리값보다 작을 경우는 설치가 가능하다.
            if arr[i] >= currenthouse + mid:
                cnt += 1
                currenthouse = arr[i]
        if cnt >= C:
            if res < mid:
                res = mid
            start = mid + 1
        else:
            end = mid -1
    return res
res = binary()
print(res)
    