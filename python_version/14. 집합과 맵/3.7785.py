n = int(input())
arr = dict()
for _ in range(n):
    name, log = map(str, input().split())
    if log == 'enter':
        arr[name] = log
    else:
        del arr[name]
temp = sorted(arr.keys(), reverse=True)
for name in temp:
    print(name)