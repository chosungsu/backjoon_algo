#-- inputs --#
box = []
for _ in range(3):
    box.append(list(map(int,input().split())))

#-- algo --#
def ccw(pos0,pos1,pos2): # 신발끈 공식에서 곱셈부분만 성립함.
    return (pos0[0]*pos1[1] + pos1[0]*pos2[1] + pos2[0]*pos0[1] - (pos1[0]*pos0[1] + pos2[0]*pos1[1] + pos0[0]*pos2[1]))

#-- result --#
ans = ccw(box[0],box[1],box[2])
if ans > 0:
    print(1)
elif ans == 0:
    print(0)
else:
    print(-1)