n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))
#        7
#      3   8
#    8   1   0
#  2   7   4   4
#4   5   2   6   5
#이와 같을 때 연산과정은 아래와 같다.
#arr[0]이고 행이 0일 때 arr[0][0] = 7
#arr[1]이고 행이 1일 때 arr[0][0] + arr[1][0] or arr[0][0] + arr[1][0] 와 같이 구할 수 있음.
#arr[2]이고 행이 2일 때 arr[1][0] + arr[2][0] or arr[1][0]/arr[1][1] 중 max + arr[2][1] or arr[1][1] + arr[2][2] 와 같이 구할 수 있음.
for j in range(1, n):
    for k in range(len(arr[j])):
        if k == 0:
            arr[j][k] += arr[j-1][k]
        elif k == j:
            arr[j][k] += arr[j-1][k-1]
        else:
            arr[j][k] += max(arr[j-1][k], arr[j-1][k-1])
            
print(max(arr[n-1]))