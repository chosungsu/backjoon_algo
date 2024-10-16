n = int(input())
copy = n
cnt = 0
while True :
    #a : 몫, b : 나머지
    a = copy // 10
    b = copy % 10
    c = (a + b) % 10
    copy = (b * 10) + c
    cnt += 1
    if (copy == n) :
        break
print(cnt)
    