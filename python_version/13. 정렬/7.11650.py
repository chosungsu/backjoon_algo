import sys
n = int(sys.stdin.readline())
list = []
for i in range(n):
    [x, y] = map(int, input().split())
    list.append([x, y])
#x값을 기준으로 정렬
res = sorted(list)
for i in range(n):
    print(res[i][0], res[i][1])