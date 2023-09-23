N = int(input())
rgb = []
# 각 집의 rgb를 리스트에 담는다.
for i in range(N):
    rgb.append(list(map(int, input().split())))
#(26, 40, 83)
#(49, 60, 57)
#(13, 89, 99)
#이와 같을 때 rgb 각 값에 대하여 다른 색의 값 중 최소값을 더해가는 과정이 필요하다.
for j in range(1,N):
    rgb[j][0] += min(rgb[j-1][1], rgb[j-1][2])
    rgb[j][1] += min(rgb[j-1][0], rgb[j-1][2])
    rgb[j][2] += min(rgb[j-1][0], rgb[j-1][1])
#마무리로 rgb의 최소값을 출력한다.
res = min(rgb[N-1])
print(res)