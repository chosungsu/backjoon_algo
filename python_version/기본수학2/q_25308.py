import sys
from itertools import permutations
import math

#-- inputs --#
input=sys.stdin.readline
arr=list(map(int, input().split()))

#-- algo --#
def check_block(x, y, z):
    x_d = float(x)
    y_d = float(y) * math.sqrt(2.0) / 2.0
    z_d = float(z)

    return y_d + (z_d / x_d) * y_d - z_d >= 0

def is_block(a):
    order = [0, 1, 2, 3, 4, 5, 6, 7]

    for i in range(8):
        x = a[order[i]]
        y = a[order[(i + 1) % 8]]
        z = a[order[(i + 2) % 8]]

        if not check_block(x, y, z):
            return False

    return True

def solution(a):
    ans = 0

    for order in permutations(range(8)):
        if is_block([a[i] for i in order]):
            ans += 1

    return ans

#-- result --#
result = solution(arr)
print(result)
