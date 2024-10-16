import sys
n = int(sys.stdin.readline())
res_list = []
for _ in range(n) :
    res_list.append(list(sys.stdin.readline().split()))
#나이 > 가입순 정렬
res_list.sort(key = lambda member : int(member[0]))
for member in range(len(res_list)) :
    print(res_list[member][0], res_list[member][1])