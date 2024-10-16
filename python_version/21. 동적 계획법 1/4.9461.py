#p(1) : 1
#p(2) : 1
#p(3) : 1
#p(4) : 2=p(1) + p(2)
#p(5) : 2=p(2) + p(3)
#p(6) : 3=p(3) + p(4)
#p(7) : 4
#p(8) : 5
#p(9) : 7
#p(10) : 9
#해당 알고리즘은 p(n) : p(n-3) + p(n-2)

N = int(input())
P = [0] * (101)
P[1] = 1
P[2] = 1
P[3] = 1
for i in range(4, 101):
    P[i] = P[i-3] + P[i-2]
for j in range(N):
    n = int(input())
    print(P[n])