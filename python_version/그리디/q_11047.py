import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = [int(input()) for _ in range(N)]
coin = 0

#가장 큰수로 나눠보기 위하여 역순정렬한다.
arr.sort(reverse=True)

#coin은 사용횟수를 기록하기 위하여 몫을 사용하고 K는 나머지로 변경된다.
for a in arr:
    coin += K // a
    K = K % a
print(coin)