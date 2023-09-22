from collections import deque
import sys

def cmd_1(deq, X):
    deq.appendleft(X)

def cmd_2(deq, X):
    deq.append(X)

def cmd_3(deq):
    if deq:
        return deq.popleft()
    return -1

def cmd_4(deq):
    if deq:
        return deq.pop()
    return -1

def cmd_5(deq):
    return len(deq)

def cmd_6(deq):
    if deq:
        return 0
    return 1

def cmd_7(deq):
    if deq:
        return deq[0]
    return -1

def cmd_8(deq):
    if deq:
        return deq[-1]
    return -1

N = int(input())
deq = deque()

commands = {
    '1': cmd_1,
    '2': cmd_2,
    '3': cmd_3,
    '4': cmd_4,
    '5': cmd_5,
    '6': cmd_6,
    '7': cmd_7,
    '8': cmd_8
}

for _ in range(N):
    command = sys.stdin.readline().split()
    cmd = command[0]

    if cmd in ['1', '2']:
        X = int(command[1])
        commands[cmd](deq, X)
    else:
        result = commands[cmd](deq)
        print(result)
