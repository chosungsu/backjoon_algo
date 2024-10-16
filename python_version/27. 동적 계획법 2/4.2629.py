import sys

input = sys.stdin.readline
N = int(input())
chu = list(map(int, input().split()))
M = int(input())
target = list(map(int, input().split()))
# d[i][j]: i번째까지 추를 사용했을 때 j무게를 만들 수 있는지 여부
d = [[False] * 15001 for _ in range(31)]

def sol(n ,w):
    # 입력받는 n
    if n > N:
        return
    # 이미 true로 만들어져 있으면 return
    if d[n][w]:
        return
    d[n][w] = True
    
    # 3가지 연산이 존재
    # 추의 무게를 더함
    # 추의 무게를 뺌
    # 추를 사용하지 않음
    sol(n + 1, w + chu[n - 1])
    sol(n + 1, abs(w - chu[n - 1]))
    sol(n + 1, w)
sol(0,0)
for t in target:
    if t > 15000:
        print('N', end=' ')
    elif d[N][t]:
        print('Y', end=' ')
    else:
        print('N', end=' ')