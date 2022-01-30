import sys
n = int(input())
check_list = [0] * 10001
for i in range(n) :
    input_num = int(sys.stdin.readline())
    check_list[input_num] = check_list[input_num] + 1
for j in range(len(check_list)) :
    if check_list[j] != 0 :
        for k in range(check_list[j]) :
            print(j)