a = int(input())
for i in range(a) :
    #floor : 층, num : 호
    floor = int(input())
    num = int(input())
    fo = [x for x in range(1, num + 1)]
    for j in range(floor) :
        for k in range(1, num) :
            fo[k] += fo[k - 1]
    print(fo[-1])