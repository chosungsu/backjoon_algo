while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    #두번째 숫자를 첫번째 숫자로 나눈 나머지가 0인 경우
    #약수이므로 factor 반환
    if b % a == 0:
        print('factor')
    #첫번째 숫자를 두번째 숫자로 나눈 나머지가 0인 경우
    #약수이므로 multiple 반환
    elif a % b == 0:
        print('multiple')
    #둘 다 아닌 경우 neither 반환
    else:
        print('neither')