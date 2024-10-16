import sys

input = sys.stdin.readline
N, C = map(int, input().split())
arr = list(map(int, input().split()))

# 냅색 문제이지만 기존의 방법과 달리 Meet in the middle 알고리즘을 사용해보자.
# 아래의 brute_force 함수는 브루트포스 알고리즘이다.
def brute_force(index, w, things, size, result):
    if index >= size:
        result.append(w)
        return
    brute_force(index + 1, w, things, size, result)
    brute_force(index + 1, w+things[index], things, size, result)

# 아래의 binary_search 함수는 이분탐색 알고리즘이다.
def binary_search(start, end, key, arr):
    while start < end :
        mid = (start + end) // 2
        if arr[mid] <= key:
            start = mid + 1
        else :
            end = mid
    return end

# 전체적으로 2로 나누어 이분탐색에 활용한다.
a_things = arr[:N // 2]
b_things = arr[N // 2:]
a_result, b_result = [], []

brute_force(0, 0, a_things, len(a_things), a_result)
brute_force(0, 0, b_things, len(b_things), b_result)

b_result.sort()
b_len = len(b_result)
cnt = 0

for i in a_result:
    # 무게를 초과하는 경우
    if C - i < 0 :
        continue
    cnt += binary_search(0,b_len,C-i,b_result)
print(cnt)