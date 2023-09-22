import sys

start = 0
def cutting(start, line):
    if line == 1:
        return
    for i in range(start + (line//3), start + (line//3) * 2):
        lines[i] = ' '
    cutting(start, (line//3))
    cutting(start + (line//3) * 2, (line//3))
while True:
    try:
        N = int(sys.stdin.readline())
        end = 3**N
        lines = ['-'] * end
        cutting(start, end)
        print(''.join(lines))
    except:
        break