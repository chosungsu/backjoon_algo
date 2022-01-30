all_list = list(range(2,246912))
memo = []
n = int(input())
def sosu(n):
    if n == 1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

for i in all_list:
    if sosu(i):
        memo.append(i)

while True:
    count=0
    #0일 때 멈춤
    if n == 0 :
        break
    for i in memo:			#memo리스트 중에서
        if n < i <=2*n:		#입력한 값의 범위 내에서 값이 있으면
            count+=1		#있을 때 마다 카운트 +1
    print(count)
    n = int(input())		#0 입력받기 전까지 계속 해야하므로 입력 받음