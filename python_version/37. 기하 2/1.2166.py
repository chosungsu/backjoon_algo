import sys

#-- inputs --#
input = sys.stdin.readline
arr_x,arr_y = [],[] # 좌표 저장
N = int(input())
for _ in range(N):
    x,y = map(int,input().split())
    arr_x.append(x)
    arr_y.append(y)
    
#-- algo --#
arr_x.append(arr_x[0])
arr_y.append(arr_y[0])
xr,yr = 0,0
for i in range(N): # 신발끈 정리
    xr+=arr_x[i]*arr_y[i+1]
    yr+=arr_y[i]*arr_x[i+1]

#-- result --#
print(round(abs((xr-yr)/2),1))