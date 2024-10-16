t = int(input())
for i in range(t) :
    floor = int(input())
    num = int(input())
    num_list = [x for x in range(1, num + 1)]
    for j in range(floor) :
        for k in range(1, len(num_list)) :
            num_list[k] += num_list[k - 1]
    print(num_list[-1])