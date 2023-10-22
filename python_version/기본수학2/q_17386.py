import sys

#-- inputs --#
input=sys.stdin.readline
x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())
l1=[[x1, y1], [x2, y2]]
l2=[[x3, y3], [x4, y4]]

#-- algo --#
def ccw(X1, X2, X3):
    tmp = (X2[0]-X1[0])*(X3[1]-X1[1])-(X2[1]-X1[1])*(X3[0]-X1[0])
    if tmp > 0:
        return 1
    elif tmp < 0:
        return -1
    else:
        return 0

#-- result --#
ans = 0
res = ccw(l1[0], l1[1], l2[0]) * ccw(l1[0], l1[1], l2[1]) < 0 and ccw(l2[0], l2[1], l1[0]) * ccw(l2[0], l2[1], l1[1]) < 0
if res:
    ans = 1
print(ans)