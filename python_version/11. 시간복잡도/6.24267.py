def MenOfPassion(A, n):
    sums = 0
    for i in range(1, n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                sums += A[i] * A[j] * A[k]
    return sums
n = int(input())
print(int((n * (n - 1) * (n - 2)) / 6))
print(3)