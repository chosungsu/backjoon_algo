n = int(input())
numbers = map(int, input().split())
sosu = 0
for num in numbers:
    ph = 0
    if num > 1 :
        for i in range(2, num):  # 2부터 n-1까지
            if num % i == 0:
                ph += 1  # 2부터 n-1까지 나눈 몫이 0이면 ph가 증가
        if ph == 0:
            sosu += 1  # ph가 없으면 소수.
print(sosu)