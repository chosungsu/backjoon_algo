a = int(input())
arr = []
for i in range(a):
    arr = list(input())
    sum = 0
    cnt = 1
    for i in arr:
        if i == 'O':
            sum += cnt
            cnt += 1
        else:
            cnt = 1
    print(sum)