def MenOfPassion(A, n):
    sums = 0
    for i in range(1, n):
        for j in range(1, n):
            for k in range(1, n):
                sums += A[i] * A[j] * A[k]
    return sums
n = int(input())
print(n**3)
print(3)