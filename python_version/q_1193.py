a = int(input())
line = 1
#제시된 숫자가 line보다 작을 때까지 반복
while a > line :
    a -= line
    line+=1
if line % 2 == 0 :
    b = a
    c = line - a + 1
else :
    b = line - a + 1
    c = a
print(b, '/', c, sep='')