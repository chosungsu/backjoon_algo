def binary_search(num):
    left = 0
    right = n-1
    while left <= right :
        mid = (left+right)//2
        if card[mid] == num :
            return 1
        elif card[mid] > num :
            right = mid - 1
        else:
            left = mid + 1
    return 0
import sys
input = sys.stdin.readline
# 상근이가 가지고 있는 숫자카드 개수 읽기
n = int(input())
# 상근이의 수 읽기
card = list(map(int, input().split()))
# 정렬하기
card.sort()
# 서치할 카드 수 읽기
m = int(input())
# 서치할 수 읽고 이진법 서치 돌리기
for num in list(map(int, input().split())):
    print(binary_search(num), end = ' ')