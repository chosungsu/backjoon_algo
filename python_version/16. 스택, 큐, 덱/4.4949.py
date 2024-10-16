while True:
    n = input()
    arr = []
    
    if n == '.':
        break
    for strs in n:
        if strs == '[' or strs == '(':
            arr.append(strs)
        elif strs == ']':
            if len(arr) != 0 and arr[-1] == '[':
                arr.pop()
            else:
                arr.append(']')
                break
        elif strs == ')':
            if len(arr) != 0 and arr[-1] == '(':
                arr.pop()
            else:
                arr.append(')')
                break
    if len(arr) == 0:
        print('yes')
    else:
        print('no')