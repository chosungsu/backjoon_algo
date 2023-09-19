T = int(input())
cent_li = [25, 10, 5, 1]

for i in range(T):
    cent = int(input())
    for j in cent_li:
        #몫을 출력
        print(cent // j, end=' ')
        #나머지로 다시 변환
        cent = cent % j