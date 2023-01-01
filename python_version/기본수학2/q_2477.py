k = int(input())
s = [list(map(int, input().split()))[1] for i in range(6)]
index = 0
max_box = 0
for i in range(6):
    if s[i%6] * s[(i+1)%6] > max_rec:
        max_box = s[i%6] * s[(i+1)%6]
        index = i
min_box = s[(index+3)%6] * s[(index+4)%6]
print(k * (max_box - min_box))