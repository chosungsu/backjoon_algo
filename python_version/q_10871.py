x, y = map(int, input().split())
A = list(map(int, input().split()))
for i in range(x) :
    if A[i] < y :
        print(A[i], end=' ')