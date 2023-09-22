import sys

N = int(sys.stdin.readline())
arr = []
for _ in range(N):
    q = sys.stdin.readline().split()
    if q[0] == '1':
        arr.append(q[1])
    elif q[0] == '2':
        if len(arr) == 0:
            print(-1)
        else:
            print(arr.pop())
    elif q[0] == '3':
        print(len(arr))
    elif q[0] == '4':
        print(1 if len(arr) == 0 else 0)
    else:
        print(-1 if len(arr) == 0 else arr[-1])