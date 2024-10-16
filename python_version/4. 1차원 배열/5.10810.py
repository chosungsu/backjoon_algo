N, M = map(int, input().split())
# 바구니 초기화
basket = [0 for _ in range(N)]

# 바구니에 공을 넣는 반복문
for _ in range(M):
    i, j, k = map(int, input().split())
    for n in range(i, j + 1):
        basket[n-1] = k
        
# 바구니에 들어있는 공 번호 출력
for i in range(N):
    print(basket[i], end=' ')