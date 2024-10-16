def MenOfPassion(A, n):
    sums = 0
    for i in range(1, n - 1):
        for j in range(i + 1, n):
            sums += A[i] * A[j]
    return sums
n = int(input())
print(n*(n-1) // 2)
print(2)