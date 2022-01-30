import sys
n = int(sys.stdin.readline())
list = []
for i in range(n):
    [x, y] = map(int, input().split())
    list.append([y, x])
#y값을 기준으로 정렬
res = sorted(list)
for i in range(n):
    print(res[i][1], res[i][0])