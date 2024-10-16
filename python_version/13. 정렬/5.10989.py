import sys
n = int(input())
check_list = [0] * 10001
for _ in range(n) :
    inputs = int(sys.stdin.readline())
    check_list[inputs] = check_list[inputs] + 1
for i in range(len(check_list)) :
    if check_list[i] != 0 :
        for _ in range(check_list[i]) :
            print(i)