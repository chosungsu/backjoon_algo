import sys
n = int(input())
list = []
for _ in range(n):
    list.append(int(sys.stdin.readline()))
list.sort()
for i in list:
    print(i)