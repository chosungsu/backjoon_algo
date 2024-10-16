a = int(input())
bag = 0
while a >= 0 :
    #5의 배수일 경우
    if a % 5 == 0 :
        bag += (a // 5)
        print(bag)
        break
    #5의 배수가 아니면 3씩 줄여나간다.
    a -= 3
    bag += 1
else :
    print(-1)