a = int(input())
nums_bee = 1
cnt = 1
while a > nums_bee :
    #벌집이 6의 배수만큼 증가
    nums_bee += 6 * cnt
    cnt += 1
print(cnt)