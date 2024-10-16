import math

# 1. 초기에 반복할 T값 읽기
T = int(input())
# 2. T만큼 반복하기
for _ in range(T):
    N, M = map(int, input().split())
    bridge = math.factorial(M) // (math.factorial(N) * math.factorial(M - N))
    print(bridge)