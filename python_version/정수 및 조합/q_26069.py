N = int(input())
arr = {'ChongChong'}
for i in range(N):
    A, B = map(str, input().split())
    if A in arr:
        arr.add(B)
    if B in arr:
        arr.add(A)
print(len(arr))