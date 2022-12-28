def sosu(n):
    if n == 1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
#입력값의 2배 범위를 리스트화
all_list = list(range(2,246912))
#전체 범위 내의 소수를 미리 리스트에 담기
memo = []
for i in all_list:
    if sosu(i):
        memo.append(i)
while True:
    count=0
    n = int(input())
    #0일 때 멈춤
    if n == 0 :
        break
    for i in memo:
        if n < i <=2*n:
            count+=1
    print(count)