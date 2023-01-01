import sys
n = int(sys.stdin.readline())
inputlist = []
for _ in range(n):
    inputs = list(map(int, input().split()))
    inputlist.append([inputs[1], inputs[0]])
res = sorted(inputlist)
for i in range(n):
    print(res[i][1], res[i][0])