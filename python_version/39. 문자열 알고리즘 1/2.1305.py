import sys

#-- inputs --#
input = sys.stdin.readline
L = int(input())
screen = str(input().strip())

#-- algo --#
def getL():
    length = len(screen)
    tmp = [0]*(length)
    j = 0

    for i in range(1, length):
        while j > 0 and screen[i] != screen[j]:
            j = tmp[j - 1]

        if screen[i] == screen[j]:
            j += 1
            tmp[i] = j

    return L - tmp[-1]

#-- result --#
print(getL())