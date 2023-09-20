def MenOfPassion(A, n):
    sums = 0
    for i in range(1, n):
        for j in range(1, n):
            sums += A[i] * A[j]
    return sums
n = int(input())
print(n**2)
print(2)