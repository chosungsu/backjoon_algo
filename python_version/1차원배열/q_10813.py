N, M = map(int, input().split())
# 바구니 초기화(N값으로)
basket = [i for i in range(1, N + 1)]
tmp = 0

# 바구니에 공을 넣는 반복문
for _ in range(M):
    i, j = map(int, input().split())
    temp = basket[i-1]
    basket[i-1]=basket[j-1]
    basket[j-1]=temp

for b in basket:
    print(b, end=' ')