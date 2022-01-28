num = int(input())
for i in range(1, num + 1) :
    n = sum((map(int, str(i))))
    res = i + n
    if res == num :
        print(i)
        break
    if i == num :
        print(0)