#마지막 줄이 0 0 0일 때까지 반복함.
while True:
        a = list(map(int, input().split()))
        #가장 긴변의 길이 구하기
        max_num = max(a)
        if sum(a) == 0:
                break
        a.remove(max_num)
        if a[0] ** 2 + a[1] ** 2 == max_num ** 2:
                print('right')
        else:
                print('wrong')