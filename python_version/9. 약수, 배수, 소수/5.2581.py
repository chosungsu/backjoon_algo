start_num = int(input())
last_num = int(input())
#소수들을 리스트로 담는다.
sosu_list = []
#시작과 마지막 수 사이의 범위 내에서 반복문 실행.
for num in range(start_num, last_num+1):
    error = 0
    if num > 1 :
        for i in range(2, num):  # 2부터 num-1까지
            # 2부터 num-1까지 나눈 몫이 0이면 error가 증가하고 for문을 끝냄
            if num % i == 0:
                error += 1
                break
        # error가 없으면 소수리스트에 추가
        if error == 0:
            sosu_list.append(num)
if len(sosu_list) > 0 :
    print(sum(sosu_list))
    print(min(sosu_list))
else:
    print(-1)