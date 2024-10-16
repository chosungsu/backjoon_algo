T = int(input())


for _ in range(T):
    arr = []
    isVPS = True
    str_li = input()
    for strs in str_li:
        if strs == '(':
            arr.append(strs)
        elif strs == ')':
            if arr:
                arr.pop()
            else:
                isVPS = False
                break
    if not arr and isVPS:
        print('YES')
    else:
        print('NO')