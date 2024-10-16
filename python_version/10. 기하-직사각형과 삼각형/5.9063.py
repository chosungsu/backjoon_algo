N = int(input())
arr_x = []
arr_y = []

for _ in range(N):
    x, y = map(int, input().split())
    arr_x.append(x)
    arr_y.append(y)
print((max(arr_x) - min(arr_x)) * (max(arr_y) - min(arr_y)))
    