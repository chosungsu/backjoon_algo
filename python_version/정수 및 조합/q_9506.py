while True:
    
    n = int(input())
    temp = []
    if n == -1:
        break
    
    for i in range(1,n): # 이렇게 되면 자기 자신은 제외한 나머지 성립
        if n % i == 0: # 약수를 저장하는 부분 
            temp.append(i)
    
    if sum(temp) == n: # 약수를 모두 더한 합이  == n이랑 같으면, 즉, 완전수인경우
        print(n, "=", end = ' ')
        print(*temp, sep = ' + ')
    else:
        print("%d is NOT perfect." %n)
        