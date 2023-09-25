import sys

input = sys.stdin.readline
N = int(input())
arr1 = list(map(int, input().split()))
M = int(input())
arr2 = list(map(int, input().split()))

# 탐색을 위해 기준이 되는 arr1을 정렬한다.
arr1.sort()

# 문제에서 의도한 이분탐색
def binary(target):
    # 왼쪽, 오른쪽의 인덱스를 설정
    left = 0
    right = N - 1

    while left <= right:
        mid = (left + right) // 2
        if arr1[mid] == target:
            return True

        if target < arr1[mid]:
            right = mid-1
        elif target > arr1[mid]:
            left = mid + 1

for i in range(M):
    if binary(arr2[i]):
        print(1)
    else:
        print(0)