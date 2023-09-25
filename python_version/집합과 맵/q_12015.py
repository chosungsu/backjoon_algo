import sys

input = sys.stdin.readline
N = int(input())
num = list(map(int, input().split()))
memorization = [0]

for x in num:
    #증가하는 것만 저장됨
    if memorization[-1] < x:
        memorization.append(x)
    else:
    #중간에 값을 넣어야 하는 경우
        start = 0
        end = len(memorization)

        while start < end:
            mid = (start+end)//2

            if memorization[mid] < x:
                start = mid + 1
            else:
                end = mid
        memorization[end] = x
print(len(memorization)-1)
    