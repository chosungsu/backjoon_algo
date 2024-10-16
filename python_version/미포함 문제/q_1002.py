#조규현의 좌표 (x1, y1)와 백승환의 좌표 (x2, y2)가 주어지고, 
#조규현이 계산한 류재명과의 거리 r1과 
#백승환이 계산한 류재명과의 거리 r2가 주어졌을 때, 
#류재명이 있을 수 있는 좌표의 수를 출력하는 프로그램을 작성하시오.
import math
n = int(input())
for i in range(n):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    #두 원의 거리 : distance(원의 방정식 사용)
    distance = math.sqrt((x1-x2)**2 + (y1-y2)**2)
    # 두 원이 동심원이고 반지름이 같을 때
    if distance == 0 and r1 == r2 :
        print(-1)
    # 내접, 외접일 때
    elif abs(r1-r2) == distance or r1 + r2 == distance:
        print(1)
    # 두 원이 서로다른 두 점에서 만날 때
    elif abs(r1-r2) < distance < (r1+r2) :
        print(2)
    else:
        print(0)