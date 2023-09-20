N = 3
sum = 0
arrs = []
for _ in range(N):
    tmp = int(input())
    arrs.append(tmp)
    sum += tmp
arrs = list(set(arrs))
if sum != 180:
    print('Error')
else:
    if len(arrs) == 3:
        print('Scalene')
    elif len(arrs) == 2:
        print('Isosceles')
    else:
        print('Equilateral')