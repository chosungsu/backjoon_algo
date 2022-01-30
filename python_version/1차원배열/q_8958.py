a = int(input())
for i in range(a):
    b = input()
    #s : b를 리스트에 담기
    s = list(b)
    sum = 0
    cnt = 1
    for i in s:
        if i == 'O':
            sum += cnt
            cnt += 1
        else:
            cnt = 1
    print(sum)