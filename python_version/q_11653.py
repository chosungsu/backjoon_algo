N = int(input())
n = 2
while N > 1:
    #2로 나눈 나머지가 0인 경우 2로 나눈다.
    if N%n == 0:
        N //= n
        print(n)
    #2로 나눈 나머지가 0이 아닌 경우.
    else:
        n += 1