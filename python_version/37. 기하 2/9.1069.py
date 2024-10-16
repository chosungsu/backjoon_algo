import sys

#-- inputs --#
input=sys.stdin.readline
x, y, d, t = map(int, input().split())
distance = (x ** 2 + y ** 2) ** 0.5

#-- algo --#
if distance >= d:
    ans = min(t * (distance // d) + distance % d, t * (distance // d + 1), distance)
else:
    ans = min(t + (d - distance), 2 * t, distance)

#-- result --#
print(ans)